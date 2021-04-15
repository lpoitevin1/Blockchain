import uuid
import time
from hashlib import sha256
import json
from Block import Block
import datetime



class Blockchain :
    def __init__(self):
        self.chain_block = []
        self.pending_transaction = []

    def get_last_block(self):
        if len(self.chain_block) == 0 :
            self.chain_block.append(Block(None, True))
        return self.chain_block[-1]
    

    def add_transaction(self, sdr, dst, data):
        self.get_last_block().add_transaction(sdr,dst,data)
    


blockchain = Blockchain()
blockchain.add_transaction('John','Jane','120')
blockchain.add_transaction('John','Jane','1201')
blockchain.get_last_block().resume()