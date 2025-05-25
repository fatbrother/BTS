const hre = require("hardhat");

async function main() {
    const ConcertTicketNFT = await hre.ethers.getContractFactory("ConcertTicketNFT");
    const concertTicketNFT = await ConcertTicketNFT.deploy();

    const address = await concertTicketNFT.getAddress();

    console.log("ConcertTicketNFT deployed to:", address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });