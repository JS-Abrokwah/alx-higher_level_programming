#!/usr/bin/python3
def safe_print_division(a, b):
    res = None
    try:
        res = round(a/b, 1)
        print("Inside result: {}".format(res))
    except (TypeError, ZeroDivisionError):
        print("Inside result: {}".format(res))
    finally:
        return res
