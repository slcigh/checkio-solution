from functools import reduce
from operator import mul

"""
functools.reduce(function, iterable[, initializer])
Apply function of two arguments cumulatively to the items of sequence, from left to right,
so as to reduce the sequence to a single value. For example,
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
calculates ((((1+2)+3)+4)+5). The left argument, x,
is the accumulated value and the right argument, y, is the update value from the sequence.
If the optional initializer is present, it is placed before the items of
the sequence in the calculation, and serves as a default when the sequence is empty.
If initializer is not given and sequence contains only one item, the first item is returned.
"""


def checkio(number):
    return reduce(mul, (int(x) for x in str(number) if x != '0'))


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
