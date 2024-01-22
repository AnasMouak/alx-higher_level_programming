#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct = fct(*args)
    except (ZeroDivisionError, IndexError) as e:
        fct = None
        print("Exception: {}".format(e), file=sys.stderr)
    return fct
