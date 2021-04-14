import hashlib
import json 


class Blockchain :
    def __init__(self):
        self.chain = []
        self.pending_transaction = []
        self.new_block(previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.", proof=100)


    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transaction = []
        self.chain.append(block)
        return block

    @property
    def get_last_block(self):
        return self.chain[-1]
    

    def add_transaction(self, sender, dst, amount):
        transaction = {
            'sender': sender ,
            'dst': dst,
            'amount':amount, 
        }
        self.pending_transaction.append(transaction)    
        return self.get_last_block['index'] + 1 

    
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        print(string_object)
        block_string = string_object.encode()
        print(block_string)

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash


b = Blockchain()
b.add_transaction('John','Jane','100')
b.add_transaction('Jane','David','200')
b.new_block(12345)

print("Blockchain :", b.chain)
