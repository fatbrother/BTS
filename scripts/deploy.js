const hre = require("hardhat");

async function main() {
    const ConcertTickets = await hre.ethers.getContractFactory("ConcertTickets");
    const concertTickets = await ConcertTickets.deploy();
    const address = await concertTickets.getAddress();

    console.log("ConcertTickets deployed to:", address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });