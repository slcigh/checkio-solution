def count_inversion(sequence):
    return sum(sum(m < n for m in sequence[i + 1:]) for i, n in enumerate(sequence))


"""
import itertools as it
​
def count_inversion(sequence):
    return sum(x > y for x, y in it.combinations(sequence, 2))
"""

"""

def count_inversion(sequence):
    head, *tail = sequence
    if tail:
        return sum(head > item for item in tail) + count_inversion(tail)
    else:
        return 0
"""
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
