import math
from itertools import zip_longest


def convert(value, from_base=10, to_base=2):
    value = math.floor(value)
    if value == 0:
        return 0
    if to_base == 10:
        res = 0
        power = 0
        for i in reversed(list(str(value))):
            i = int(i)
            res += i * (from_base ** power)
            power += 1
        return res
    if from_base != 10:
        value = convert(value, from_base=from_base, to_base=10)
    symbols = []
    while value > 0:
        symbols.append(value % to_base)
        value //= to_base
    symbols.reverse()
    return int(''.join(map(str, symbols)))


assert convert(0) == 0
assert convert(1) == 1
assert convert(33) == 100001
assert convert(23) == 10111

assert convert(16, to_base=4) == 100
assert convert(28, to_base=3) == 1001

assert convert(56, from_base=7, to_base=10) == 41
assert convert(12, from_base=3, to_base=10) == 5

assert convert(35, from_base=8, to_base=2) == 11101
assert convert(13, from_base=4, to_base=3) == 21
assert convert(10, from_base=2, to_base=5) == 2
