class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.current = 0
        self.capacity = capacity

    def append(self, item):
        if len(self.data) != self.capacity:
            self.data.append(item)
        else:
            self.data[self.current] = item
            self.current = (self.current+1) % self.capacity

    def get(self):
        return self.data
