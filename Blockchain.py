from Block import Block

class Blockchain:
    # genesis_block = None
    # current_block = None
    def __init__(self):
        #initialize the genesis block
        self.genesis_block = Block(None, "genesis")
        self.current_block = self.genesis_block
        
    def print_blockchain(self):
        curr = self.current_block
        while curr:
            print(curr.index)
            curr = curr.prev_index