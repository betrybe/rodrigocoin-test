from abc import ABC, abstractmethod


class Importer(ABC):
    @staticmethod
    @abstractmethod
    def import_data(filename):
        """
        Imports data from file.

        Args:
            filename (str): path to filename

        Returns:
            list: a list of items (dict) loaded from the file
        """

        pass


def assert_file_extension(filename, extension):
    """
    Raises exception in case the filename does not match the extension

    Args:
        filename (str): path to filename
        extension (str): extension to be checked (without the '.')
    """
    if filename.split('.')[-1].lower() != extension.lower():
        raise ValueError("Arquivo inválido")
