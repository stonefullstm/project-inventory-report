from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(1, "Azeite", "Trás-os-Montes Azeites",
                      "18-02-2021", "17-09-2023", "AZ25 1551 4467 2549 4402 1",
                      "em lugar fresco e seco")
    assert str(produto) == (
            "O produto Azeite fabricado em 18-02-2021 "
            "por Trás-os-Montes Azeites com validade até 17-09-2023 precisa "
            "ser armazenado em lugar fresco e seco."
        )
