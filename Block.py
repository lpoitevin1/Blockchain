from time import time
import json
import datetime
from hashlib import sha256


class Block :
    def __init__(self, index, time, dst, rcv, amount):
        self.index = index
        self.time = time
        self.dst = dst 
        self.rcv = rcv
        self.amount = amount
    
    def compute_hash(self):
        # Dump json object
        block_object = json.dumps(self.__dict__, sort_keys=True)
        hashing_block = sha256(block_object.encode()).hexdigest()
        print(hashing_block)
        return hashing_block
    


b = Block(0,'ez','John','Jane','100')
b.compute_hash()