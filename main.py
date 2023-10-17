import configparser
from web3 import Web3
import time
import requests

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

PRIVATE_KEY = config['DEFAULT']['PRIVATE_KEY']
Bearer_key = config['DEFAULT']['BEARER_KEY']
CONTRACT_ADDRESS = config['DEFAULT']['CONTRACT_ADDRESS']
REFERRER_ADDRESS = config['DEFAULT']['REFERRER_ADDRESS']

# Setup Connection
w3 = Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))
# Ensure connectivity
if not w3.isConnected():
    print("Not connected!")
    exit()

# Set up your account (using private key)
account = w3.eth.account.privateKeyToAccount(PRIVATE_KEY)
w3.eth.defaultAccount = account.address

wallet_address = account.address


#CONTRACT_ADDRESS = "0x9c8574779468125975f370b7746fb2af7cb13fdb" #Old Contract
#CONTRACT_ADDRESS = "0x563395A2a04a7aE0421d34d62ae67623cAF67D03" #New Contract
#CONTRACT_ADDRESS = "" #If there have new addres, put in here.

def sell_shares(address, count):
    #TRADING CONTRACT ADDRESS
    method_id = '0xaac35d87' #Sell Method with Refferer

    # Parameters
    Sell_address = address
    value = count
    # Referrer Address, I set my address for some referrer funds if you would like to donate me. If not change to your address
    # 邀請碼地址, 我設置了我自己的邀請碼, 如果你願意donate我幫妳寫這個腳本的話, 如果不要請更改成自己的地址
    Ref_address = REFERRER_ADDRESS

    # Encode parameters
    encoded_address1 = w3.toBytes(hexstr=Sell_address).rjust(32, b'\0').hex()
    encoded_value = w3.toBytes(value).rjust(32, b'\0').hex()
    encoded_address2 = w3.toBytes(hexstr=Ref_address).rjust(32, b'\0').hex()

    # Combine the method ID and the encoded parameters
    input_data = method_id + encoded_address1 + encoded_value + encoded_address2

    transaction = {
        'chainId': 43114,
        'to': CONTRACT_ADDRESS,
        'from': wallet_address, #Input Your ADDRESS here
        'data': input_data,
        'gas': 200000,
        'gasPrice': w3.toWei('25', 'gwei'),
        'nonce':  w3.eth.getTransactionCount(account.address),
    }

    signed_tx = w3.eth.account.signTransaction(transaction, PRIVATE_KEY)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    if receipt["status"] == 1:
        return True
    else:
        return False



def main():
    url = "https://api.starsarena.com/shares/holdings"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {Bearer_key}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    # Ensure you handle potential errors
    if response.status_code == 200:
        data = response.json()
        for i in data["holdings"]:
            sell_address = i["subjectUser"]["address"]
            sell_amount = i["amount"]
            sell_username = i["subjectUser"]["twitterName"]
            sell_status = sell_shares(i["subjectUser"]["address"],1)
            if sell_status:
                print (f"Sell {sell_amount} keys of {sell_username} Success!")
            else:
                print (f"Sell {sell_amount} keys of {sell_username} Fail!")
    else:
        print(f"Request failed with status code {response.status_code}")

if __name__ == "__main__":
    main()