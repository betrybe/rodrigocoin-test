import csv

from inventory_report.importer.importer import Importer, assert_file_extension


class CsvImporter(Importer):
    @staticmethod
    def import_data(filename):
        assert_file_extension(filename, 'csv')

        with open(filename) as f:
            return list(csv.DictReader(f))
