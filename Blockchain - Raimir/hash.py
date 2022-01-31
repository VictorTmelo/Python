from hashlib import sha256
from datetime import datetime

class Hash:

    def __init__(self):
        self.blocks = []
        self.set_genesis_block()

    def set_genesis_block(self):
        data = 'Bloco Genesis'
        timestamp = datetime.utcnow().timestamp()
        prev_hash = 0
        index = 0
        self.hash_block(
            data, timestamp, prev_hash, index
        )

    def hash_block(self, data, timestamp, prev_hash, index):
        hash = ''
        nonce = 1
        while not self.is_hash_valid(hash):
            block = '{}:{}:{}:{}:{}'.format(
                data, timestamp, prev_hash, index, nonce
            )
            hash = sha256(block.encode()).hexdigest()
            nonce += 1
        print('[nonce]', nonce)
        self.blocks.append(hash)

    def add_new_block(self, data):
        index = len(self.blocks)
        prev_hash = self.get_last_hash()
        timestamp = datetime.utcnow().timestamp()
        self.hash_block(
            data, timestamp, prev_hash, index
        )

    def get_last_hash(self):
        return self.blocks[-1]

    def is_hash_valid(self, hash):
        return hash.startswith('000')

    def get_all(self):
        return self.blocks[:]