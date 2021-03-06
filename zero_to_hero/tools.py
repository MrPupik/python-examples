
__doc__ = "this module contains varoous tools"
from datetime import date, datetime

# built in modules:
# import sys
# import os

# modules from pypi (install using `pip install module_name`)
# paramiko
# requests


def input_int(num_range: tuple):
    """
    `range`: tuple like (from, to)
    """
    frm, to = num_range
    option = input(f'enter number between {frm} and {to} ')
    while (not option.isdigit()) or (int(option) < frm or int(option) > to):
        print("Error: invalid option")
        option = input()
    return int(option)


def cool():
    print("la la la ")


def print_this_time():
    """should be used only when this modle is the main module"""
    print(datetime.now())


if __name__ == '__main__':
    print_this_time()
