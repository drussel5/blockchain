import datetime

class Block:
    # index = None
    # curr_hash = None
    # prev_hash = None
    # time_stamp = None
    # data = None
    
    def __init__(self, prev_index, data):
        self.index = [prev_index + 1] if prev_index is not None else 0
        self.prev_index = prev_index
        self.curr_hash = hash(self.index)
        self.prev_hash = hash(prev_index)
        self.time_stamp = datetime.datetime.now()
        self.data = data + str(self.index)
        
        