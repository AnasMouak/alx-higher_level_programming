#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and tuple_b:
        x = tuple_a[0] + tuple_b[0]
        y = tuple_a[1] + (tuple_b[1] if len(tuple_b) > 1 else 0)
        return (x, y)
    elif tuple_a:
        return tuple_a
    elif tuple_b and len(tuple_b) > 1:
        return tuple_b
    else:
        return ()
