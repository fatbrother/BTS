import argparse
import json
from web3 import Web3


def load_contract_interface(abi_path, bytecode_path=None):
    with open(abi_path, 'r', encoding='utf-8') as f:
        contract_json = json.load(f)
    abi = contract_json.get('abi')
    bytecode = contract_json['bytecode']
    return abi, bytecode


def sign_hold_event(rpc_url, private_key, abi_path, bytecode_path,
                    event_name, total_tickets, start_time, end_time, whitelist):
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    account = w3.eth.account.from_key(private_key)

    abi, bytecode = load_contract_interface(abi_path, bytecode_path)
    factory = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Build deployment transaction
    construct_txn = factory.constructor(
        event_name,
        total_tickets,
        start_time,
        end_time,
        whitelist
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
                whitelist
            ).build_transaction({
                'from': account.address,
                'nonce': w3.eth.get_transaction_count(account.address),
            })['data']
        }),
    })

    signed = w3.eth.account.sign_transaction(construct_txn, private_key)
    # Return rawTransaction without '0x'
    return signed.raw_transaction.hex()[2:]


def sign_reserve_event(rpc_url, private_key, abi_path, contract_address):
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    account = w3.eth.account.from_key(private_key)

    abi, _ = load_contract_interface(abi_path)
    contract = w3.eth.contract(address=contract_address, abi=abi)

    txn = contract.functions.reserveTicket().buildTransaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': w3.eth.estimate_gas({
            'from': account.address,
            'to': contract_address,
            'data': contract.encodeABI(fn_name='reserveTicket')
        }),
    })

    signed = w3.eth.account.sign_transaction(txn, private_key)
    return signed.rawTransaction.hex()[2:]


def main():
    parser = argparse.ArgumentParser(description='Sign ConcertTickets transactions')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # holdEvent command
    hold = subparsers.add_parser('holdEvent', help='Sign a holdEvent (deploy) transaction')
    hold.add_argument('--rpc-url', required=True, help='RPC endpoint URL')
    hold.add_argument('--private-key', required=True, help='User private key')
    hold.add_argument('--abi', required=True, help='Path to contract JSON with ABI & bytecode')
    hold.add_argument('--event-name', required=True)
    hold.add_argument('--total-tickets', type=int, required=True)
    hold.add_argument('--start-time', type=int, required=True, help='Unix timestamp')
    hold.add_argument('--end-time', type=int, required=True, help='Unix timestamp')
    hold.add_argument('--whitelist', nargs='+', required=True, help='List of addresses to whitelist')

    # reserveEvent command
    reserve = subparsers.add_parser('reserveEvent', help='Sign a reserveEvent transaction')
    reserve.add_argument('--rpc-url', required=True, help='RPC endpoint URL')
    reserve.add_argument('--private-key', required=True, help='User private key')
    reserve.add_argument('--abi', required=True, help='Path to contract JSON with ABI')
    reserve.add_argument('--contract-address', required=True, help='Deployed contract address')

    args = parser.parse_args()

    if args.command == 'holdEvent':
        raw_tx = sign_hold_event(
            args.rpc_url,
            args.private_key,
            args.abi,
            args.abi,  # reuse JSON for both ABI and bytecode
            args.event_name,
            args.total_tickets,
            args.start_time,
            args.end_time,
            args.whitelist
        )
    elif args.command == 'reserveEvent':
        raw_tx = sign_reserve_event(
            args.rpc_url,
            args.private_key,
            args.abi,
            args.contract_address
        )
    else:
        parser.error('Unknown command')

    print(raw_tx)


if __name__ == '__main__':
    main()