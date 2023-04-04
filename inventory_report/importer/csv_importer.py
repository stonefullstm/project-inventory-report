from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".csv"):
            stock_list = []
            with open(path, 'r') as file:
                stock_dict = csv.DictReader(file)
                for product in stock_dict:
                    stock_list.append(product)
                return stock_list
        else:
            raise ValueError("Arquivo inválido")
