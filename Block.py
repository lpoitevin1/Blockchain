from time import time
import json
import datetime
from hashlib import sha256
import uuid


class Block :
    def __init__(self, previous_hash, first=False):
        self.transactions = []
        self.pending_transaction = []
        
        if first : 
            self.previous_hash = None
        else:
            self.previous_hash = previous_hash
        self.hash_id = self.compute_hash()
        self.proof = False
    
    def compute_hash(self):
        # Dump json object
        block_object = json.dumps(self.__dict__, sort_keys=True)
        hashing_block = sha256(block_object.encode()).hexdigest()
        print(hashing_block)
        return hashing_block


    def add_transaction(self, sender, dst, data) :
        time = datetime.datetime.now().strftime('%m/%d/%Y')
        transaction = {
            'id': uuid.uuid4().hex,
            'time':time,
            'sender':sender,
            'dst':dst,
            'data':data,
            'proof': False
        }
        
        self.pending_transaction.append(transaction)
        return transaction
    

    def resume(self):
        print('[*] Pending transaction: \r\n')
        for transaction in self.pending_transaction :
            print(json.dumps(transaction))
        
        print('\r\n[*] Pending transaction confirmed: \r\n')
        for transaction in self.transactions:
            print(json.dumps(transaction))
        

    

