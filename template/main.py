# Setup
import asyncio
import json
import datetime

from web3 import Web3

alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/JnpFQC29V9ymhUzqRcmhmoM60726U9OX"

w3 = Web3(Web3.HTTPProvider(alchemy_url))

eth_usd_contract = '0x37bC7498f4FF12C19678ee8fE19d713b87F6a9e6'
link_eth_contract = '0xbba12740DE905707251525477bAD74985DeC46D2'
usdt_eth_contract = '0x7De0d6fce0C128395C488cb4Df667cdbfb35d7DE'
abi = json.loads(open('abi').readlines()[0])
addresses_contract = [eth_usd_contract, link_eth_contract, usdt_eth_contract]
addresses_names = ["eth_usd", "link_eth", "usdt_eth"]
contracts = [w3.eth.contract(address=c_address, abi=abi) for c_address in addresses_contract]


def handle_event(event, name):
    jn = json.loads(Web3.toJSON(event))
    print("{} :::: |{}| current: {}; roundId: {}; updatedAt: {}; ".format(str(datetime.datetime.now()),
                                                                          name,
                                                                          jn['args']['current'],
                                                                          jn['args']['roundId'],
                                                                          jn['args']['updatedAt']))


async def log_loop1(event_filter, poll_interval, id_contract_name):
    print("Start connection with {}, {}".format(addresses_names[id_contract_name], str(event_filter)))
    while True:
        for AnswerUpdated in event_filter.get_new_entries():
            handle_event(AnswerUpdated, addresses_names[id_contract_name])
        await asyncio.sleep(poll_interval)


def main():
    events = [contract.events.AnswerUpdated.createFilter(fromBlock='latest') for contract in contracts]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(*[log_loop1(events[i], 1, i) for i in range(len(events))]))
    finally:
        loop.close()


if __name__ == "__main__":
    main()
