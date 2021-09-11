from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    REPORT_FMT = (
        "{simple_report}\n"
        "Produtos estocados por empresa:\n"
        "{prods_per_comp}"
    )

    PRODS_PER_COMP_FMT = "- {company}: {count}\n"

    @classmethod
    def generate(cls, data):
        """
        Generates a complete report from the data provided.
        The complete report includes the simple report (SimpleReport)
        and adds further information.

        Args:
            data (list): a list of items(dict)

        Returns:
            str: the formatted report
        """
        prods_count = cls._get_prods_count(data)

        return CompleteReport.REPORT_FMT.format(
            simple_report=super()._generate(data, prods_count),
            prods_per_comp=cls._generate_prods_per_comp(prods_count)
        )

    @classmethod
    def _generate_prods_per_comp(cls, prods_count):
        return ''.join([
            cls.PRODS_PER_COMP_FMT.format(company=company, count=count)
            for company, count in prods_count.items()
        ])
