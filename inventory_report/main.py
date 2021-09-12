import sys

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor

EXT_IMPORTER = {
    'csv': CsvImporter,
    'json': JsonImporter,
    'xml': XmlImporter
}


def _print_report(filename, report_type):
    ext = filename.split('.')[-1].lower()
    importer = EXT_IMPORTER[ext]

    inventory = InventoryRefactor(importer)
    report = inventory.import_data(filename, report_type)

    print(report, end='')


def main():
    """
    Receives filename and report type from command line
    and prints the corresponding report.
    """
    if len(sys.argv) != 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    _print_report(
        filename=sys.argv[1],
        report_type=sys.argv[2]
    )
