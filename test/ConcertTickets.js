const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("ConcertTickets", function () {
    let ConcertTickets, concertTickets, issuer, otherAccount;

    beforeEach(async function () {
        ConcertTickets = await ethers.getContractFactory("ConcertTickets");
        [issuer, otherAccount] = await ethers.getSigners();
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
                concertTickets.connect(otherAccount).setEventDetails(totalTickets, startTime, endTime)
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
});

describe("reserveTicket", function () {
    let ConcertTickets, concertTickets, issuer, otherAccount;

    beforeEach(async function () {
        ConcertTickets = await ethers.getContractFactory("ConcertTickets");
        [issuer, otherAccount] = await ethers.getSigners();
        concertTickets = await ConcertTickets.deploy();
        await concertTickets.waitForDeployment();
    });

    it("Should reserve ticket", async function () {
        const totalTickets = 100;
        const startTime = Math.floor(Date.now() / 1000);
        const endTime = startTime + 86400;

        await concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime);
        await concertTickets.connect(otherAccount).reserveTicket();

        const reservations = await concertTickets.getReservations();
        expect(reservations).to.include(otherAccount.address);
    });

    it("Should prevent reservation before reservation period", async function () {
        const totalTickets = 100;
        const startTime = Math.floor(Date.now() / 1000) + 86400; // 1天後開始
        const endTime = startTime + 86400;

        await concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime);

        await expect(
            concertTickets.connect(otherAccount).reserveTicket()
        ).to.be.revertedWith("Reservation period not started");
    });

    it("Should prevent reservation after reservation period", async function () {
        const totalTickets = 100;
        const startTime = Math.floor(Date.now() / 1000);
        const endTime = startTime + 86400;

        await concertTickets.connect(issuer).setEventDetails(totalTickets, startTime, endTime);

        await ethers.provider.send("evm_setNextBlockTimestamp", [endTime + 1]);

        await expect(
            concertTickets.connect(otherAccount).reserveTicket()
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

        await concertTickets.connect(otherAccount).reserveTicket();

        await network.provider.send("evm_setNextBlockTimestamp", [startTime + 200]);
        await network.provider.send("evm_mine");

        await expect(
            concertTickets.connect(otherAccount).reserveTicket()
        ).to.be.revertedWith("Already reserved");
    });
});