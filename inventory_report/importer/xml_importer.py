import xmltodict

from inventory_report.importer.importer import Importer, assert_file_extension


class XmlImporter(Importer):
    @staticmethod
    def import_data(filename):
        """
        Imports data from XML file.

        Args:
            filename (str): path to filename

        Returns:
            list: a list of items (dict) loaded from the file
        """

        assert_file_extension(filename, 'xml')

        with open(filename, 'rb') as f:
            parsed_data = xmltodict.parse(f)
            # force each item to be a dict
            return [
                dict(item)
                for item in parsed_data['dataset']['record']
            ]
