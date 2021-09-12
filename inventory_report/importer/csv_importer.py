import csv

from inventory_report.importer.importer import Importer, assert_file_extension


class CsvImporter(Importer):
    @staticmethod
    def import_data(filename):
        """
        Imports data from CSV file.

        Args:
            filename (str): path to filename

        Returns:
            list: a list of items (dict) loaded from the file
        """

        assert_file_extension(filename, 'csv')

        with open(filename) as f:
            # force each item to be a dict
            return [
                dict(item)
                for item in csv.DictReader(f)
            ]
