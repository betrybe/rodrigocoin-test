from collections import Counter, OrderedDict
from datetime import date


class SimpleReport:
    REPORT_FMT = (
        "Data de fabricação mais antiga: {oldest_fab}\n"
        "Data de validade mais próxima: {closest_exp}\n"
        "Empresa com maior quantidade de produtos estocados: {most_prods}\n"
    )

    @classmethod
    def generate(cls, data):
        return cls._generate(
            oldest_fab=cls._find_oldest_fab(data),
            closest_exp=cls._find_closest_exp(data),
            most_prods=cls._find_most_prod_comp(cls._get_prods_count(data)),
        )

    @classmethod
    def _generate(cls, oldest_fab, closest_exp, most_prods):
        return SimpleReport.REPORT_FMT.format(
            oldest_fab=oldest_fab,
            closest_exp=closest_exp,
            most_prods=most_prods,
        )

    @classmethod
    def _find_oldest_fab(cls, data):
        fab_dates = [
            date.fromisoformat(item['data_de_fabricacao'])
            for item in data
        ]

        return min(fab_dates).isoformat()

    @classmethod
    def _find_closest_exp(cls, data):
        exp_dates = [
            date.fromisoformat(item['data_de_validade'])
            for item in data
        ]

        today = date.today()
        exp_dates = [dt for dt in exp_dates if dt >= today]

        return min(exp_dates).isoformat()

    @classmethod
    def _find_most_prod_comp(cls, prods_count):
        # most_common always returns a list with a tuple (key, count)
        # so we get the top item and return the key
        return prods_count.most_common(1)[0][0]

    @classmethod
    def _get_prods_count(cls, data):
        return OrderedCounter([
            item['nome_da_empresa']
            for item in data
        ])


# Class created from python documentation
class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)
