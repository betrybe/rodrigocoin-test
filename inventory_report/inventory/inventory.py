import csv
import json

import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(filename, report_type):
        data = _import_data(filename)

        if report_type == 'simples':
            return SimpleReport.generate(data)
        elif report_type == 'completo':
            return CompleteReport.generate(data)
        else:
            raise ValueError(
                "Tipo de relatório desconhecido: {}".format(report_type)
            )


def _import_data_from_csv(filename):
    with open(filename) as f:
        return list(csv.DictReader(f))


def _import_data_from_json(filename):
    with open(filename) as f:
        return json.load(f)


def _import_data_from_xml(filename):
    with open(filename, 'rb') as f:
        parsed_data = xmltodict.parse(f)
        return parsed_data['dataset']['record']


EXT_METHODS = {
    'csv': _import_data_from_csv,
    'json': _import_data_from_json,
    'xml': _import_data_from_xml,
}


def _import_data(filename):
    ext = filename.split('.')[-1].lower()
    import_method = EXT_METHODS[ext]
    return import_method(filename)
