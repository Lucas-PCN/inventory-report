from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def read_file(cls, path):
        with open(path) as file:
            if path.endswith(".csv"):
                return list(csv.DictReader(file))
            elif path.endswith(".json"):
                return json.load(file)
            elif path.endswith(".xml"):
                return xmltodict.parse(file.read())["dataset"]["record"]
            else:
                raise ValueError('Invalid format file')

    @classmethod
    def import_data(cls, file, type):
        report_data = cls.read_file(file)

        if type == "simples":
            return SimpleReport.generate(report_data)
        elif type == "completo":
            return CompleteReport.generate(report_data)
        else:
            raise ValueError("Tipo inválido")
