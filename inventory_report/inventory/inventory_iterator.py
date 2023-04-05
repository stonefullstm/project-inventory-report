from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __next__(self):
        item = self.data[self.index]
        if not item:
            raise StopIteration

        self.index += 1
        return item
