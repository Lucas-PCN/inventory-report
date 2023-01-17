from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def products_by_company(report_list):
        report_text = ""
        companies_list = Counter(
            product["nome_da_empresa"] for product in report_list
        )

        for company, amount in companies_list.items():
            report_text += f"- {company}: {amount}\n"
        return report_text

    @staticmethod
    def generate(report_list: list):

        simple_report = SimpleReport.generate(report_list)

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{CompleteReport.products_by_company(report_list)}"
        )
