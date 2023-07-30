import json
from web3 import Web3
import time
from loguru import logger

def wallet():
    with open('wallets.txt', 'r') as f:
        wallets = f.read().splitlines()
        return wallets

rpc = 'https://rpc.zora.co/'  # Вставить РПС евм сети где проверить баланс нативного токена

def resfile_clean():
    with open("results.txt", "w") as file:
        pass

def check():
    resfile_clean()
    wallets = wallet()
    web3 = Web3(Web3.HTTPProvider(rpc))
    logger.info(rpc)
    for i, account in enumerate(wallets):
        acc_chk = web3.to_checksum_address(account)
        balance = web3.eth.get_balance(acc_chk)
        bal_eth = round(web3.from_wei(balance, "ether"),7)
        if bal_eth > 0:
            with open("results.txt", "a") as file:
                file.write(acc_chk + '  ' + str(bal_eth) + "\n")
            logger.info(f'{i+1}    {acc_chk}  sum = {str(bal_eth)}')
        else:
            logger.info(f'{i+1}    {acc_chk}  sum = 0')
        time.sleep(2)

if __name__ == '__main__':
    check()

