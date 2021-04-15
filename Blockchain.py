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
        return chain_block[-1]
    
    def add_transaction(self, sender, dst, data) :
        time = datetime.datetime.now().strftime('%m/%d/%Y')
        transaction = {
            'time':time,
            'sender':sender,
            'dst':dst,
            'data':data,
            'proof': False
        }
        if len(self.chain_block) > 0:
            previous_hash = self.chain_block[-1].hash_id
            block = Block(previous_hash,transaction, False)
        else:
            block = Block(None, transaction , True)
        
        self.pending_transaction.append(block)
        return block


blockchain = Blockchain()
blockchain.add_transaction('John','Jane','120')
blockchain.add_transaction('John','Jane','1201')