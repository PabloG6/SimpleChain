import hashlib
import time


class BlockChain:
    def __init__(self, index, previous_hash, **wallet_transactions):
        self.wallet_transactions = wallet_transactions
        self.index = index
        self.previous_hash = previous_hash

    def hash(self):
        # hashing function created for block

        # get current timestamp
        timestamp = time.time()
        self.hash = hashlib.sha256(str(timestamp).encode())
        print(self.hash.hexdigest())

        pass


if __name__ == "__main__":
    init_time_stamp = time.time()
    first_hash = hashlib.md5(str(init_time_stamp).encode())

    first_block = BlockChain(0, first_hash)
    print(str(first_block.previous_hash.hexdigest()))
