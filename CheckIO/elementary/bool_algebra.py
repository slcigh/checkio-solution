OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    results = {"conjunction": x and y,
               "disjunction": x or y,
               "implication": y or not x,
               "exclusive": x ^ y,
               "equivalence": x == y
               }
    return results[operation]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
