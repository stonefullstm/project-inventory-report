from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        result = self.importer.import_data(path)
        self.data = list(result)

    def __iter__(self):
        return InventoryIterator(self.data)
