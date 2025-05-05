const hre = require("hardhat");

async function main() {
    totalTickets = 100;
    startTime = Math.floor(Date.now() / 1000);
    endTime = startTime + 86400;

    const Account = await hre.ethers.getSigners();
    const whitelist = [
        Account[0].address,
        Account[1].address,
        Account[2].address,
        Account[3].address,
        Account[4].address,
    ];
    const ConcertTickets = await hre.ethers.getContractFactory("ConcertTickets");
    const concertTickets = await ConcertTickets.deploy(
        "Concert Ticket",
        totalTickets,
        startTime,
        endTime,
        whitelist
    );
    const address = await concertTickets.getAddress();

    console.log("ConcertTickets deployed to:", address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });