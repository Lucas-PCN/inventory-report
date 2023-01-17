from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(reportList: list):

        today = datetime.now().strftime('%Y-%m-%d')

        oldest_date = min(
            [product["data_de_fabricacao"] for product in reportList]
        )

        closest_date = min([product["data_de_validade"]
                            for product in reportList
                            if product["data_de_validade"] > today])

        bigger_company, _ = Counter([product["nome_da_empresa"]
                                    for product in reportList]
                                    ).most_common()[0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {bigger_company}"
        )
