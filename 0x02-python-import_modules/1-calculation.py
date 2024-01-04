#!/usr/bin/python3
if __name__ == "__main__":

    import calculator_1 as func

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, func.add(a, b)))
    print("{} - {} = {}".format(a, b, func.sub(a, b)))
    print("{} * {} = {}".format(a, b, func.mul(a, b)))
    print("{} / {} = {}".format(a, b, func.div(a, b)))
