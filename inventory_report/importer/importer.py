from abc import ABC, abstractmethod


class Importer(ABC):
    @staticmethod
    @abstractmethod
    def import_data(filename):
        pass


def assert_file_extension(filename, extension):
    if filename.split('.')[-1].lower() != extension.lower():
        raise ValueError("Arquivo inválido")
