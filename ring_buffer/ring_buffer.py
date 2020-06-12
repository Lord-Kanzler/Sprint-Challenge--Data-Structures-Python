class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)

        else:
            self.storage[self.index] = item
            self.index += 1
            if self.index > (self.capacity - 1):
                self.index = 0

    def get(self):
        return [val for val in self.storage if val is not None]
