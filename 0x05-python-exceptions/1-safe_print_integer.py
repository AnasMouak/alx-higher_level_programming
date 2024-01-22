#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value):
            print("{:d}".format(value))
            return True
    except (ValueError, TypeError):
        return False
