def add(*args):
    total = 0
    print(type(args))
    for inp in args:
        total += inp
    return total



print(add(1, 2, 3, 4, 10, 9))
