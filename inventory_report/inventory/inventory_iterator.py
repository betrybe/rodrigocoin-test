class InventoryIterator:
    def __init__(self, data):
        self.data = data
        self.curr = 0

    def __iter__(self):
        return self

    def __next__(self):
        curr = self.curr
        if self.curr >= len(self.data):
            raise StopIteration

        self.curr += 1

        return self.data[curr]
