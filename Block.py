from time import time
import json
import datetime
from hashlib import sha256


class Block :
    def __init__(self, previous_hash, transaction, first=False):
        self.transactions = []
        self.pending_transaction = []
        
        if first : 
            self.previous_hash = None
        else:
            self.previous_hash = previous_hash
        self.pending_transaction.append(transaction)
        self.hash_id = self.compute_hash()
        self.proof = False
    
    def compute_hash(self):
        # Dump json object
        block_object = json.dumps(self.__dict__, sort_keys=True)
        hashing_block = sha256(block_object.encode()).hexdigest()
        print(hashing_block)
        return hashing_block
    

    

