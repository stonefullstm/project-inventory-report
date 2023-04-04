from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".xml"):
            with open(path, 'r') as file:
                data_dict = xmltodict.parse(file.read())
                return data_dict["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")
