from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path.endswith('.csv'):
            stock_list = cls.read_csv(path)
            return cls.select_report(stock_list, type)
        elif path.endswith('.json'):
            stock_list = cls.read_json(path)
            return cls.select_report(stock_list, type)
        else:
            pass

    @classmethod
    def read_csv(cls, path):
        stock_list = []
        with open(path, 'r') as file:
            stock_dict = csv.DictReader(file)
            for product in stock_dict:
                stock_list.append(product)
        return stock_list

    @classmethod
    def read_json(cls, path):
        with open(path, 'r') as file:
            return json.load(file)

    @classmethod
    def select_report(cls, stock_list, type):
        if type == "simples":
            return SimpleReport.generate(stock_list)
        elif type == "completo":
            return CompleteReport.generate(stock_list)
