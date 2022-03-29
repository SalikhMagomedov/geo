import os

_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def get_root_path() -> str:
    return _ROOT_PATH


def get_geo_chem_file_path() -> str:
    return os.path.join(_ROOT_PATH, 'data/geo_chem_9-13.xlsx')
