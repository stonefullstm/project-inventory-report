from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, stock_data):
        oldest_manufacturing_date = min(
            [product["data_de_fabricacao"] for product in stock_data])

        nearest_expiration_date = min(
            [product["data_de_validade"] for product in stock_data
                if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                >= datetime.today()])

        # source: https://acervolima.com/
        #   python-contar-ocorrencias-de-um-elemento-em-uma-lista/
        cias = Counter(product["nome_da_empresa"] for product in stock_data)
        # source: https://datagy.io/python-get-dictionary-key-with-max-value/
        cia_with_more_products = max(cias, key=cias.get)

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {cia_with_more_products}"
        )
