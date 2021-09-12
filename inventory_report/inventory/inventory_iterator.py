class InventoryIterator:
    """
    Iterates over an inventory data.
    """

    def __init__(self, data):
        """
        Args:
            data (list): the data to be iterated over

        Attributes:
             data (list): the data provided
             curr (int): index of where the iterator is
        """

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
