from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import sys


def get_stock_data(path, type):
    if path.endswith('.csv'):
        return InventoryRefactor(CsvImporter)
    elif path.endswith('.json'):
        return InventoryRefactor(JsonImporter)
    elif path.endswith('.xml'):
        return InventoryRefactor(XmlImporter)


def main():
    try:
        _, path, type = sys.argv

        stock_data = get_stock_data(path, type)
        stock_data.import_data(path, type)
        if (type == "simples"):
            sys.stdout.write(SimpleReport.generate(stock_data.data))
        elif (type == "completo"):
            sys.stdout.write(CompleteReport.generate(stock_data.data))

    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")
