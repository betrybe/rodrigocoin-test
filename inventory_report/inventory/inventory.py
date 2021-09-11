import csv
import json

import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(filename, report_type):
        """
        Loads data from file and returns a report from that data.

        Args:
            filename (str): path to file
            report_type (str): type of the report, either 'simples' or 'completo'

        Returns:
            str: report formatted according to its type
        """
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
    """
    Imports data from CSV file.

    Args:
        filename (str): path to filename

    Returns:
        list: a list of items (dict) loaded from the file
    """

    with open(filename) as f:
        return list(csv.DictReader(f))


def _import_data_from_json(filename):
    """
    Imports data from JSON file.

    Args:
        filename (str): path to filename

    Returns:
        list: a list of items (dict) loaded from the file
    """

    with open(filename) as f:
        return json.load(f)


def _import_data_from_xml(filename):
    """
    Imports data from XML file.

    Args:
        filename (str): path to filename

    Returns:
        list: a list of items (dict) loaded from the file
    """

    with open(filename, 'rb') as f:
        parsed_data = xmltodict.parse(f)
        return parsed_data['dataset']['record']


EXT_METHODS = {
    'csv': _import_data_from_csv,
    'json': _import_data_from_json,
    'xml': _import_data_from_xml,
}


def _import_data(filename):
    """
    Imports data from file.

    Args:
        filename (str): path to filename

    Returns:
        list: a list of items (dict) loaded from the file
    """

    ext = filename.split('.')[-1].lower()
    import_method = EXT_METHODS[ext]
    return import_method(filename)
