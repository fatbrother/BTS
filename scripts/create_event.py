import sys
import os
import time
import json
from web3 import Web3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import Event, User, db, load_contract_interface, app

# 1. 連線到本地 Hardhat 節點
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# 2. get account（Hardhat default account[0]）
deployer = w3.eth.accounts[0]

# 3. initial event details
event_name = "My Concert"
total_tickets = 100
start_time = int(time.time()) + 3600
end_time = start_time + 7200
whitelist = [deployer]  # 你可以加更多地址

# 4. load contract ABI 和 bytecode
abi, bytecode = load_contract_interface()

# 5. create contract
Concert = w3.eth.contract(abi=abi, bytecode=bytecode)
nft_address = '0x5FbDB2315678afecb367f032d93F642f64180aa3'  # 依你的需求修改
construct_txn = Concert.constructor(
    event_name,
    total_tickets,
    start_time,
    end_time,
    whitelist,
    nft_address
).build_transaction({
    'from': deployer,
    'nonce': w3.eth.get_transaction_count(deployer),
    'gas': 3000000,
    'gasPrice': w3.eth.gas_price,
})

# 6. 用本地節點自動簽名並發送
tx_hash = w3.eth.send_transaction(construct_txn)
print("Deploying contract...")
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = receipt.contractAddress
print(f"Contract deployed at: {contract_address}")

# 7. 寫入資料庫
with app.app_context():
    # 取得 user（這裡假設 deployer address 已註冊為 User）
    user = User.query.filter_by(address=deployer).first()
    if not user:
        print("Deployer address not found in User table.")
        sys.exit(1)
    event = Event(
        name=event_name,
        start_time=start_time,
        end_time=end_time,
        total_tickets=total_tickets,
        contract_address=contract_address,
        owner_id=user.id
    )
    db.session.add(event)
    db.session.commit()
    print(f"Event '{event_name}' created and saved to DB.")
