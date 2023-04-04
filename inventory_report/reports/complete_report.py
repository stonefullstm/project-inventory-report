from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, stock_data):
        companies = Counter(
            product["nome_da_empresa"] for product in stock_data)

        header = "Produtos estocados por empresa:"
        details = ""
        for company in companies:
            details += f"- {company}: {companies[company]}\n"

        return (
            f"{super().generate(stock_data)}\n"
            f"{header}\n"
            f"{details}"
        )
