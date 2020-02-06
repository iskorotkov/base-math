from itertools import zip_longest


def plus(a, b, base=2):
    a = list(map(int, list(str(a))))
    b = list(map(int, list(str(b))))
    res = []
    overflow = 0
    for (x, y) in zip_longest(reversed(a), reversed(b)):
        if x is None:
            val = y + overflow
        elif y is None:
            val = x + overflow
        else:
            val = (x + y + overflow)
        res.append(val % base)
        overflow = val // base
    if overflow != 0:
        res.append(overflow)
    res.reverse()
    return int(''.join(map(str, res)))


assert plus(1, 1) == 10
assert plus(10, 1) == 11
assert plus(110010, 1110) == 1000000

assert plus(23, 54, base=10) == 77
assert plus(899, 101, base=10) == 1000

assert plus(345, 1, base=6) == 350
