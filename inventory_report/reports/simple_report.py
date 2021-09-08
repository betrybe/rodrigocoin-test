from collections import Counter
from datetime import date


class SimpleReport:
    REPORT_FMT = (
        "Data de fabricação mais antiga: {oldest_fab}\n"
        "Data de validade mais próxima: {closest_exp}\n"
        "Empresa com maior quantidade de produtos estocados: {most_prods}\n"
    )

    @staticmethod
    def generate(data):
        return SimpleReport.REPORT_FMT.format(
            oldest_fab=SimpleReport._find_oldest_fab(data),
            closest_exp=SimpleReport._find_closest_exp(data),
            most_prods=SimpleReport._find_most_prod_comp(data),
        )

    @staticmethod
    def _find_oldest_fab(data):
        fab_dates = [
            date.fromisoformat(item['data_de_fabricacao'])
            for item in data
        ]

        return min(fab_dates).isoformat()

    @staticmethod
    def _find_closest_exp(data):
        exp_dates = [
            date.fromisoformat(item['data_de_validade'])
            for item in data
        ]

        today = date.today()
        exp_dates = [dt for dt in exp_dates if dt >= today]

        return min(exp_dates).isoformat()

    @staticmethod
    def _find_most_prod_comp(data):
        product_count = Counter([
            item['nome_da_empresa']
            for item in data
        ])

        # most_common always returns a list with a tuple (key, count)
        # so we get the top item and return the key
        return product_count.most_common(1)[0][0]
