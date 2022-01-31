from hashlib import sha256
from datetime import datetime
from typing import List

class Blockchain:

    def __init__(self):
        self.blocks: List[Block] = []
        self.set_genesis_block()

    def set_genesis_block(self):
        dd = self.generate_hash('Genesis', datetime.utcnow().timestamp(), 'previous_hash', 0)
        genesis = Block(0, 'Genesis', datetime.utcnow().timestamp(), 'previous_hash', dd['hash'], dd['nonce'])
        self.blocks.append(genesis)

    def add_new_block(self, input_message: str):
        index: int = len(self.blocks)
        timestamp: float = datetime.utcnow().timestamp()
        prev_hash: str = self.get_last_hash()
        dd: dict = self.generate_hash(input_message, timestamp, prev_hash, index)
        block_hash: str = dd["hash"]
        block_nonce: int = dd["nonce"]
        new_block = Block(index, input_message, timestamp, prev_hash, block_hash, block_nonce)
        self.blocks.append(new_block)

    def generate_hash(self, message: str, timestamp: float, previous_hash: str, index: int) -> dict:
        initial_hash = ''
        nonce = 1
        while not self.is_hash_valid(initial_hash):
            block = f'{message}:{timestamp}:{previous_hash}' \
                    f':{index}:{nonce}'
            initial_hash = sha256(block.encode()).hexdigest()
            nonce += 1
        return {"nonce": nonce, "hash": initial_hash}


    def get_last_hash(self) -> str:
        return self.blocks[-1].current_hash

    def get_all_hashes(self) -> List[str]:
        return [str(i) for i in self.blocks]

    @staticmethod
    def is_hash_valid(input_hash: str):
        return input_hash.startswith('000')


class Block:

    def __init__(self, index: int, message: str, timestamp: float, previous_hash: str, current_hash: str, nonce: int):
        self.index = index
        self.message = message
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.current_hash = current_hash
        self.nonce = nonce

    def __str__(self):
        return "[Index] → {}, [Message] → {}, [Timestamp] → {}, " \
               "[Previous hash] → {}, [Current hash] → {}, [Nonce] → {}".format(self.index, self.message, self.timestamp, self.previous_hash,self.current_hash, self.nonce)

