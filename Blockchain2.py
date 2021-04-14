import uuid
import time
from hashlib import sha256
import json

class Block:
    


class Blockchain :
    def __init__(self):
        self.chain_block = []
        self.pending_transaction = []

    def new_block(self, sender, dst, amount) :
        transactions = {
            'time' : time.time()
            'index': uuid.uuid4()
            'sender': sender,
            'dst' : dst,
            'amount': amount
            'proof': False
        }
        self.pending_transaction.append(transactions)
        return transactions.index

    def hash_block(self, transactions):
        json.dump(transactions)

