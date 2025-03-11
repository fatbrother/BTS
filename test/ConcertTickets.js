const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("ConcertTickets", function () {
    let ConcertTickets, concertTickets, issuer, otherAccounts;

    beforeEach(async function () {
        ConcertTickets = await ethers.getContractFactory("ConcertTickets");
        [issuer, ...otherAccounts] = await ethers.getSigners();
        concertTickets = await ConcertTickets.deploy();
        await concertTickets.waitForDeployment();
    });

    describe("setEventDetails", function () {
        it("Should set event details", async function () {
            const totalTickets = 100;
            const startTime = Math.floor(Date.now() / 1000);
            const endTime = startTime + 86400;

            await concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime);

            expect(await concertTickets.totalTickets()).to.equal(totalTickets);
            expect(await concertTickets.reservationStart()).to.equal(startTime);
            expect(await concertTickets.reservationEnd()).to.equal(endTime);
        });

        it("Should prevent non-issuer from calling this function", async function () {
            const totalTickets = 100;
            const startTime = Math.floor(Date.now() / 1000);
            const endTime = startTime + 86400;

            await expect(
                concertTickets.connect(otherAccounts[0]).setEventDetails(totalTickets, startTime, endTime)
            ).to.be.revertedWith("Only issuer can call this function");
        });

        it("Should prevent setting event details with invalid time range", async function () {
            const totalTickets = 100;
            const startTime = Math.floor(Date.now() / 1000);
            const endTime = startTime - 1;

            await expect(
                concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime)
            ).to.be.revertedWith("Invalid time range");
        });
    });

    describe("reserveTicket", function () {
        it("Should reserve ticket", async function () {
            const totalTickets = 100;
            const startTime = Math.floor(Date.now() / 1000);
            const endTime = startTime + 86400;

            await concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime);
            await concertTickets.connect(otherAccounts[0]).reserveTicket();

            const reservations = await concertTickets.getReservations();
            expect(reservations).to.include(otherAccounts[0].address);
        });

        it("Should prevent reservation before reservation period", async function () {
            const totalTickets = 100;
            const startTime = Math.floor(Date.now() / 1000) + 86400; // 1天後開始
            const endTime = startTime + 86400;

            await concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime);

            await expect(
                concertTickets.connect(otherAccounts[0]).reserveTicket()
            ).to.be.revertedWith("Reservation period not started");
        });

        it("Should prevent reservation after reservation period", async function () {
            const totalTickets = 100;
            const startTime = Math.floor(Date.now() / 1000);
            const endTime = startTime + 86400;

            await concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime);

            await ethers.provider.send("evm_setNextBlockTimestamp", [endTime + 1]);

            await expect(
                concertTickets.connect(otherAccounts[0]).reserveTicket()
            ).to.be.revertedWith("Reservation period ended");
        });

        it("Should prevent double reservation", async function () {
            const totalTickets = 100;
            const currentBlock = await ethers.provider.getBlock("latest");
            const currentTimestamp = currentBlock.timestamp;
            const startTime = currentTimestamp + 100;
            const endTime = startTime + 86400;

            await concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime);
            await network.provider.send("evm_setNextBlockTimestamp", [startTime]);
            await network.provider.send("evm_mine");

            await concertTickets.connect(otherAccounts[0]).reserveTicket();

            await network.provider.send("evm_setNextBlockTimestamp", [startTime + 200]);
            await network.provider.send("evm_mine");

            await expect(
                concertTickets.connect(otherAccounts[0]).reserveTicket()
            ).to.be.revertedWith("Already reserved");
        });
    });

    describe("selectWinners", function () {
        it("Should let all reservations win whem totalTickets >= reservations.length", async function () {
            const totalTickets = 100;
            const currentBlock = await ethers.provider.getBlock("latest");
            const currentTimestamp = currentBlock.timestamp;
            const startTime = currentTimestamp + 100;
            const endTime = startTime + 86400;

            await concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime);
            await network.provider.send("evm_setNextBlockTimestamp", [startTime]);
            await network.provider.send("evm_mine");

            // 模擬 3 個使用者預約
            for (let i = 0; i < 3; i++) {
                await concertTickets.connect(otherAccounts[i]).reserveTicket();
            }

            // 結束預約並選取獲獎者
            await concertTickets.connect(issuer).endReservation();
            await concertTickets.connect(issuer).selectWinners(12345);

            // 驗證每個預約者都獲獎
            for (let i = 0; i < 3; i++) {
                const ticketNumber = await concertTickets.winners(otherAccounts[i].address);
                expect(ticketNumber).to.be.gt(0); // 票號大於 0 表示獲獎
            }
        });

        it("Should let random reservations win when totalTickets < reservations.length", async function () {
            const totalTickets = 2;
            const currentBlock = await ethers.provider.getBlock("latest");
            const currentTimestamp = currentBlock.timestamp;
            const startTime = currentTimestamp + 100;
            const endTime = startTime + 86400;

            await concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime);
            await network.provider.send("evm_setNextBlockTimestamp", [startTime]);
            await network.provider.send("evm_mine");

            // 模擬 5 個使用者預約
            for (let i = 0; i < 5; i++) {
                await concertTickets.connect(otherAccounts[i]).reserveTicket();
            }

            // 結束預約並選取獲獎者
            await concertTickets.connect(issuer).endReservation();
            await concertTickets.connect(issuer).selectWinners(12345);

            // 統計獲獎者數量
            let winnerCount = 0;
            for (let i = 0; i < 5; i++) {
                const ticketNumber = await concertTickets.winners(otherAccounts[i].address);
                if (ticketNumber > 0) winnerCount++;
            }
            expect(winnerCount).to.equal(2); // 確認只有 2 個獲獎者
        });

        it("Should generate different winners with different randomSeed", async function () {
            const totalTickets = 2;
            const currentBlock = await ethers.provider.getBlock("latest");
            const currentTimestamp = currentBlock.timestamp;
            const startTime = currentTimestamp + 100;
            const endTime = startTime + 86400;

            await concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime);
            await network.provider.send("evm_setNextBlockTimestamp", [startTime]);
            await network.provider.send("evm_mine");

            for (let i = 0; i < 5; i++) {
                await concertTickets.connect(otherAccounts[i]).reserveTicket();
            }

            await concertTickets.connect(issuer).endReservation();

            await concertTickets.connect(issuer).selectWinners(12345);
            const winners1 = await Promise.all(
                otherAccounts.slice(0, 5).map(async (acc) => await concertTickets.winners(acc.address))
            );

            concertTickets = await ConcertTickets.deploy();
            await concertTickets.waitForDeployment();
            await concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime);
            for (let i = 0; i < 5; i++) {
                await concertTickets.connect(otherAccounts[i]).reserveTicket();
            }
            await concertTickets.connect(issuer).endReservation();

            // 使用 randomSeed = 54321 選取獲獎者
            await concertTickets.connect(issuer).selectWinners(54321);
            const winners2 = await Promise.all(
                otherAccounts.slice(0, 5).map(async (acc) => await concertTickets.winners(acc.address))
            );

            // 確認不同 randomSeed 產生不同結果
            expect(winners1).not.to.deep.equal(winners2);
        });
    });
});
