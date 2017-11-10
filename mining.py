import hashlib
import time


from blockchain import BlockChain
class Miner:
    def __init__(self):
        pass

    def calculate_hash(self, number_of_transactions):
        # number of transactions is a list of wallet transactions from wallet
        def wallet_transactions():
            return True

        self.time_stamp = time.time()
        if wallet_transactions():
            # if wallet transactions are true then calculate time stamp and hash based on that
            # create a block and add it to the blockchain
            hash = hashlib.sha256(str(time.time()).encode())
            block = BlockChain([0, 0, 0, 0, 0], 0, hash)
            #add block
            pass

        pass

if __name__ == "__main__":
    miner = Miner()
    miner.calculate_hash(45)
