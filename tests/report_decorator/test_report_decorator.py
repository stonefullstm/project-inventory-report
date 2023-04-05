from tests.report_decorator.stock_data import data
from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
import pytest


@pytest.fixture
def mock_data():
    return data


def test_decorar_relatorio(mock_data):
    report = ColoredReport(SimpleReport)
    result = (
        "\033[32mData de fabricação mais antiga:\033[0m "
        "\033[36m2020-09-06\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m "
        "\033[36m2023-09-17\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m "
        "\033[31mTarget Corporation\033[0m"
    )

    assert report.generate(mock_data) == result
