# BlockChain Ticketing System

This is a simple ticketing system that uses the blockchain to store tickets and their information. The system is built using the Hardhat framework and Solidity.

## Installation

To install the project, clone the repository and run the following commands:

```bash
npm install
pip install -r requirements.txt
```

## Generating the contract ABI

To generate the contract ABI, use the following command:

```bash
npx hardhat compile
```

## Running the test network

To run the test network, use the following command:

```bash
npx hardhat node
```

Deploy the contract to the local network using:
use another terminal

```bash
npx hardhat run scripts/deployNFT.js --network localhost
npx hardhat run scripts/deploy.js --network localhost
```

Run flask server using:

```bash
# Windows
set FLASK_APP=app.py
# macOS/Linux
export FLASK_APP=app.py

flask run
```

Creat event

```bash
python scripts/create_event.py
```

## LICENSE

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
