import xmltodict

from inventory_report.importer.importer import Importer, assert_file_extension


class XmlImporter(Importer):
    @staticmethod
    def import_data(filename):
        assert_file_extension(filename, 'xml')

        with open(filename, 'rb') as f:
            parsed_data = xmltodict.parse(f)

            return parsed_data['dataset']['record']
