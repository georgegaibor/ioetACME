import sys
from os import path
import logging

from .common.util import employee_list, match_and_format
from . import config

level = logging.DEBUG
fmt = "[%(levelname)s] - %(message)s"
logging.basicConfig(level=level, format=fmt)


def main(argv):
    if len(argv) != 2:
        logging.error(config.add_path)
        sys.exit()
    elif path.exists(argv[1]):
        employees = employee_list(argv[1])
        match_and_format(employees)
    else:
        logging.error(config.check_exist)
        sys.exit()
