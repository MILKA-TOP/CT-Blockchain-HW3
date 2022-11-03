from web3 import Web3

ganache_url = 'https://eth-mainnet.g.alchemy.com/v2/JnpFQC29V9ymhUzqRcmhmoM60726U9OX'
web3 = Web3(Web3.HTTPProvider(ganache_url))
account_1 = '0x37bC7498f4FF12C19678ee8fE19d713b87F6a9e6'
private_key1 = '0xbba12740DE905707251525477bAD74985DeC46D2'
account_2 = '0xbba12740DE905707251525477bAD74985DeC46D2'

#get the nonce.  Prevents one from sending the transaction twice
nonce = web3.eth.getTransactionCount(account_1)

#build a transaction in a dictionary
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

#sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, "private_key1")

#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaction hash
print(web3.toHex(tx_hash))