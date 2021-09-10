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
        prods_count = cls._get_prods_count(data)
        
        simple_report = super()._generate(
            oldest_fab=cls._find_oldest_fab(data),
            closest_exp=cls._find_closest_exp(data),
            most_prods=cls._find_most_prod_comp(prods_count),
        )
        
        return CompleteReport.REPORT_FMT.format(
            simple_report=simple_report,
            prods_per_comp=cls._generate_prods_per_comp(prods_count)
        )
    
    @classmethod
    def _generate_prods_per_comp(cls, prods_count):
        return ''.join([
            cls.PRODS_PER_COMP_FMT.format(company=company, count=count)
            for company, count in prods_count.items()
        ])
