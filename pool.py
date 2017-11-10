"""
pool creates genesis block
"""
import hashlib

import time

from blockchain import BlockChain


class Pool:
    def __init__(self):
        # create genesis block
        first_hash = hashlib.md5(str(time.time()).encode())
        # no wallets currently exist for
        self.GENESIS_BLOCK = BlockChain(0, first_hash)



        pass
