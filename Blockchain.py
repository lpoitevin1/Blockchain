import hashlib
import json 
from time import time

class Blockchain :
    def __init__(self):
        self.chain = []
        self.pending_transaction = []
        self.new_block(previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.", proof=100)
