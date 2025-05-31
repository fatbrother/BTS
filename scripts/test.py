import requests
import json
from web3 import Web3
from datetime import datetime
import pytz

# Flask API base URL
API_BASE_URL = "http://127.0.0.1:5000"
NFT_ADDR = "0x5fbdb2315678afecb367f032d93f642f64180aa3"  # Replace with actual NFT contract address

# Web3 setup
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Load ConcertTickets ABI and bytecode
with open("artifacts/contracts/ConcertTickets.sol/ConcertTickets.json") as f:
    contract_json = json.load(f)
    concert_tickets_abi = contract_json["abi"]
    concert_tickets_bytecode = contract_json["bytecode"]

# Test accounts (Hardhat node accounts)
accounts = [
    {
        "username": "alice",
        "private_key": "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80",
        "address": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
    },
    {
        "username": "bob",
        "private_key": "0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d",
        "address": "0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
    },
    {
        "username": "charlie",
        "private_key": "0x5de4111afa1a4b94908f83103eb1f1706367c2e68ca870fc3fb9a804cdab365a",
        "address": "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC",
    },
    {
        "username": "dave",
        "private_key": "0x7c852118294e51e653712a81e05800f419141751be58f605c371e15141b007a6",
        "address": "0x90F79bf6EB2c4f870365E785982E1f101E93b906",
    },
    {
        "username": "eve",
        "private_key": "0x47e179ec197488593b187f80a00eb0da91f1b9d0b13f8733639f19c30a34926a",
        "address": "0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65",
    },
]

cdt_tz = pytz.timezone('Asia/Taipei')

# Event data
events = [
    {
        "name": "Tech Conference 2025",
        "start_time": int(cdt_tz.localize(datetime.strptime("Jul 15, 2025 12:00", "%b %d, %Y %H:%M")).timestamp()),
        "end_time": int(cdt_tz.localize(datetime.strptime("Jul 15, 2025 16:00", "%b %d, %Y %H:%M")).timestamp()),  # 4 hours later
        "total_tickets": 100,
        "introduction": "An annual conference for tech enthusiasts and professionals.",
        "location": "San Francisco, CA",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAQDiHA7CjjHbep5RPuRvfYAWGPlvLFAY8kqNU3pI9EsBuUVTLGC-4ELl3D3gRSN7zLFFxy3PoxL8DjmD3hMm9j_4fs6sKxfRQL3-AIT5peqH15fV-rq1pjG9HwHxPT8XbJqPZ1h9hR3nhPlptJ4Nb1IWv2xKykSusockrrz8ogmB3Yvpiv00lRGbRH5UQBiWb79COAnr4k16Sck9yrn8K8b9JuRmkvffiWsSsJP1zsJ3ziE2p6I0z0liXYCh-0qo8d9QOA9ZpdVCA",
    },
    {
        "name": "Summer Music Festival",
        "start_time": int(cdt_tz.localize(datetime.strptime("Aug 5, 2025 12:00", "%b %d, %Y %H:%M")).timestamp()),
        "end_time": int(cdt_tz.localize(datetime.strptime("Aug 5, 2025 16:00", "%b %d, %Y %H:%M")).timestamp()),  # 4 hours later
        "total_tickets": 200,
        "introduction": "A vibrant music festival featuring top artists and bands.",
        "location": "Los Angeles, CA",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuDIePY8mlM70DZ-kyYKZBmNylftHkhleSlzvL38kT68EPhqwAAAwv11byzsIvRlyCUA4t7lzcCi0CI9tNIxIeAA3aUCMx259oUKUsa2xfsSprxXqOsfwmHTlrOQRFYc7LIzJZ5Ae9P9P03hgWtFURvO0p1s-aO5kp0OnCP4lfOGIfKHtA9kFU72mDZo9sp8MibCXDJTbtsSJWL3n8iQCQUDurIhHtYoZjreWR_TB_96-NTIfFURx-ZSP5OVkQwf4pKzn_O0fy6f41U",
    },
    {
        "name": "Sports Expo",
        "start_time": int(cdt_tz.localize(datetime.strptime("Sep 20, 2025 12:00", "%b %d, %Y %H:%M")).timestamp()),
        "end_time": int(cdt_tz.localize(datetime.strptime("Sep 20, 2025 16:00", "%b %d, %Y %H:%M")).timestamp()),  # 4 hours later
        "total_tickets": 150,
        "introduction": "An expo showcasing the latest in sports technology and gear.",
        "location": "New York, NY",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuClxr-3EbfqJA-gKA1eMXrAf0wJ5t8ovIksgZ2mBjzuzUGgW0CZW78oXxQVyPAD4eq4lJ59H48QqhBzejVOKSaMdRnGeFYzrAzdkWx7vGM4dnA3wSrv4dFSk_Nt8PLrPQPQm4WI06tmVbOoV_ImVuGB-7R407jamYgaR5vX17OGOarrsbcHouKBrOMr3QSDJWB1-bzccb3aVVcL_rDiiCfWQfnMWr1UEa-K07Qgfmxpk5umgys6N19u2_HDW1FV65GieDpbKGckIh0",
    },
    {
        "name": "Art Exhibition",
        "start_time": int(cdt_tz.localize(datetime.strptime("Oct 10, 2025 08:00", "%b %d, %Y %H:%M")).timestamp()),
        "end_time": int(cdt_tz.localize(datetime.strptime("Oct 10, 2025 16:00", "%b %d, %Y %H:%M")).timestamp()),  # 8 hours later
        "total_tickets": 80,
        "introduction": "An exhibition featuring contemporary artists and their works.",
        "location": "Chicago, IL",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAZ7r9HMEms5X7s9UnQS-Hak1EdK5shLPwGY3hb1At8O_7lCS9gunTUx8Axmv1CxIUOJZYdz-fyeYxFc42H1BTBfOE2VtS2TVd2wLk5k5cvzf_Cv6zqy4hPKrgHCbC1CqBxDjSfCw18UAurJ2xLe0kvHsnSmHjSpJPy0KZ5slHKcjpMyefGrydqfWmzNWxA2j4FndaE8ZXUL_TctrytbfGSugxd_laLRQu_9HxMZAWsw_M9vjuzTso5dv2_BJn44mIsA14wxaghEA8",
    },
    {
        "name": "Food & Wine Tasting",
        "start_time": int(cdt_tz.localize(datetime.strptime("Nov 2, 2025 03:00", "%b %d, %Y %H:%M")).timestamp()),
        "end_time": int(cdt_tz.localize(datetime.strptime("Nov 2, 2025 15:00", "%b %d, %Y %H:%M")).timestamp()),  # 12 hours later
        "total_tickets": 120,
        "introduction": "A tasting event featuring gourmet food and fine wines.",
        "location": "Miami, FL",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuC2LkrS6IMldMA-mMYQ-IT6XfuyP_VOrTIIVgtRAojPpUB4wrfpCGxXylkh9h0IkpGzN9vVEubz_hS0iSdAcsL0ZT7kty4O3xqKaJhxrOgkm2_NxzPesZBE-t3V8oJptvVQEkapGSG4lb_ECCaJZzeol55Yv8HmL_mtG4BZhteQMwRhPR96Kd2S45Ckxr5C_VGx7j4_s6QMwr_QX7JS7AUGZYVRDjcLSNPsHdLqBTpCNfevtw8xZyzdh3xrwElp7qMFJ2JvrykZBt4",
    },
    {
        "name": "Business Networking Event",
        "start_time": int(cdt_tz.localize(datetime.strptime("Dec 1, 2025 10:00", "%b %d, %Y %H:%M")).timestamp()),
        "end_time": int(cdt_tz.localize(datetime.strptime("Dec 2, 2025 10:00", "%b %d, %Y %H:%M")).timestamp() + 8 * 3600),  # 8 hours later
        "total_tickets": 200,
        "introduction": "A networking event for business professionals to connect and collaborate.",
        "location": "Seattle, WA",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuDlRdkmnVnLHb5KWIzLOTQ_Ao2MtYKVG4uWV9FUGbhd4B1GE6_03BOiyDIg5Vub0r3_7s8VNvCpUBAtkNETcHaZaV_QtY2tCoDH95EQxGjVTrI7JIdcKl2PEQTJPtPw_kd5ASH1OdTfmr_h9RXCujzQK0AmrF7X8Kr-BkSTM1B7tv4lGPqOL1ds8UjYgN-PzvCnlCjVVTiRFQXrrNmxXoiRM2ZfSgurRGyaS64v_xL-E3hftxIo7WPaojkw1bf-25FXZdmxWUlq55g",
    },
    {
        "name": "Outdoor Adventure Meetup",
        "start_time": int(cdt_tz.localize(datetime.strptime("Jan 15, 2025 10:00", "%b %d, %Y %H:%M")).timestamp()),
        "end_time": int(cdt_tz.localize(datetime.strptime("Jan 15, 2025 16:00", "%b %d, %Y %H:%M")).timestamp()),  # 6 hours later
        "total_tickets": 100,
        "introduction": "A meetup for outdoor enthusiasts to explore and enjoy nature.",
        "location": "Denver, CO",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAGxBjJOSOx7SvfbD06kVgM8iqGso-m4atPBKmBlvQV9wRMo39mTXPLY24tyjX5kAeGLomj7r6bwwxCXQAKN9CJXaZrcPhkb7EOykB3hH7wbzdwFOINM6LtEKXKdBnTvoxXKs0uDSvrUSOZqNacTZaRR1DPVFRkjjYmNk6Yn7z1XYNegjs9OELXY-yRxE1VfomZwkbZy8qWo5svNIYMc8Q_5etiBtlE6w7EKzlpVAx0Pmz5EcoOTDUVSZjjQgtwrHLgkmPsc8At4QY",
    },
    {
        "name": "Charity Gala",
        "start_time": int(cdt_tz.localize(datetime.strptime("Feb 28, 2025 13:59", "%b %d, %Y %H:%M")).timestamp()),
        "end_time": int(cdt_tz.localize(datetime.strptime("Feb 28, 2025 23:59", "%b %d, %Y %H:%M")).timestamp()),  # Full day event
        "total_tickets": 250,
        "introduction": "A gala event to raise funds for charity organizations.",
        "location": "Boston, MA",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuDDOVcEwjBaVj2Q4e4wc1HD6SaELhgQD5w9tEJjGzFHFluBhnEkiQc8Ztaz8PZIca7IzlyPeIURXP7jcpBRsAp2xqlCCrkHRMf33YwsNyH6eZbVEniNgmQ-Ercz2irBCyekbi_R6orYCDQbgXV9ow09CSxdkkGrq8vGsnLIHUJLXbaeR8VX0hswOfc3WOCVTADjvAh7-nme9yJr9PiqZ5zFzHN61IoQuPMuwcc8Go4eg5xHBxUWbZLhwrssUcPUsZG_sK36GYZZug0",
    }
]

# Whitelist for events
whitelist = [acc["address"] for acc in accounts]

def sign_hold_event(private_key, event_name, total_tickets, start_time, end_time, whitelist):
    account = w3.eth.account.from_key(private_key)

    factory = w3.eth.contract(abi=concert_tickets_abi, bytecode=concert_tickets_bytecode)

    # Build deployment transaction
    construct_txn = factory.constructor(
        event_name,
        total_tickets,
        start_time,
        end_time,
        whitelist,
        Web3.to_checksum_address(NFT_ADDR)
    ).build_transaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': w3.eth.estimate_gas({
            'from': account.address,
            'data': factory.constructor(
                event_name,
                total_tickets,
                start_time,
                end_time,
                whitelist,
                Web3.to_checksum_address(NFT_ADDR)
            ).build_transaction({
                'from': account.address,
                'nonce': w3.eth.get_transaction_count(account.address),
            })['data']
        }),
    })

    signed = w3.eth.account.sign_transaction(construct_txn, private_key)
    # Return rawTransaction without '0x'
    return signed.raw_transaction.hex()

def register_users():
    print("Registering users...")
    for account in accounts:
        try:
            response = requests.post(
                f"{API_BASE_URL}/register",
                json={
                    "address": account["address"],
                }
            )
            response.raise_for_status()
            print(f"User {account['username']} registered: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to register {account['username']}: {e.response.json() if e.response else e}")


def main():
    # Register users
    register_users()

    # Login users and hold events
    for event in events:
        try:
            signed_tx = sign_hold_event(
                accounts[0]["private_key"],
                event["name"],
                event["total_tickets"],
                event["start_time"] * 1000,  # Convert to milliseconds
                event["end_time"] * 1000,  # Convert to milliseconds
                whitelist
            )
            response = requests.post(
                f"{API_BASE_URL}/holdEvent",
                json={
                    "signedTx": signed_tx,
                    "eventName": event["name"],
                    "startTime": event["start_time"] * 1000,  # Convert to milliseconds
                    "endTime": event["end_time"] * 1000,  # Convert to milliseconds
                    "introduction": event["introduction"],
                    "totalTickets": event["total_tickets"],
                    "location": event["location"],
                    "image": event["image"],
                },
            )
            response.raise_for_status()
            print(f"Event {event['name']} response: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to create event {event['name']}: {e.response.json() if e.response else e}")

if __name__ == '__main__':
    main()