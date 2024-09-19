#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1 and len(tuple_b) >= 2:
        tuple_c = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
        return tuple_c
    elif len(tuple_a) >= 2 and len(tuple_b) == 1:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
        return tuple_c
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        tuple_c = (tuple_a[0] + tuple_b[0], 0)
        return tuple_c
    elif len(tuple_a) == 0 and len(tuple_b) == 0:
        tuple_c = 0, 0
        return tuple_c
    elif len(tuple_a) >= 2 and len(tuple_b) == 0:
        return tuple_a
    elif len(tuple_a) == 0 and len(tuple_b) >= 2:
        return tuple_b
    else:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return tuple_c
