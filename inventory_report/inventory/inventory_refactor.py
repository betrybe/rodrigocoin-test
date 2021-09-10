from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        # make shallow copy of the list so the iterator
        # does not misbehave if the list is changed
        return InventoryIterator(list(self.data))

    def import_data(self, filename, report_type):
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
