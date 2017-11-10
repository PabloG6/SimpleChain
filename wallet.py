"""
used for the purpose of creating wallets and sending coins to other addresses
"""
import hashlib
import uuid


class Wallet:
    def __init__(self, address, password):
        # everybody starts off with one coin
        self.coins = 1
        # todo create a unique address for user
        salt = uuid.uuid4().hex
        self.address = hashlib.sha512(address + salt + password).hexdigest()

        pass

    def send_coins(self, address):
        # search through addresses to find location of wallet you want to send to
        if self.coins > 0:
            self.coins -= 1
            # send coin to other wallet

        pass

    def hash(self):
        pass
