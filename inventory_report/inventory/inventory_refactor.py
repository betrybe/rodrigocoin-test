from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(self, importer):
        """
        Args:
            importer (Importer): the class to be used when importing data

        Attributes:
            importer (Importer): the importer class provided
            data (list): the (cumulative) data imported
        """

        self.importer = importer
        self.data = []

    def __iter__(self):
        # make shallow copy of the list so the iterator
        # does not misbehave if the list is changed
        return InventoryIterator(list(self.data))

    def import_data(self, filename, report_type):
        """
        Loads data from file and returns a report from that data.

        The data is stored cumulatively into the 'data' attribute, so
        each call returns a report that also includes all previous data.

        Args:
            filename (str): path to file
            report_type (str): type of the report, either 'simples' or 'completo'

        Returns:
            str: report formatted according to its type

        Raises:
            ValueError: if report_type is not a valid string
        """

        self.data.extend(
            self.importer.import_data(filename)
        )

        if report_type == 'simples':
            return SimpleReport.generate(self.data)
        elif report_type == 'completo':
            return CompleteReport.generate(self.data)
        else:
            raise ValueError(
                "Tipo de relatório desconhecido: {}".format(report_type)
            )
