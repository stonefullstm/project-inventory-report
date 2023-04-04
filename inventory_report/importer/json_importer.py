from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".json"):
            with open(path, 'r') as file:
                return json.load(file)
        else:
            raise ValueError("Arquivo inválido")
