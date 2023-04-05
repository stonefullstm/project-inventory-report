from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        result = self.importer.import_data(path)
        for item in result:
            self.data.append(item)

    def __iter__(self):
        return InventoryIterator(self.data)
