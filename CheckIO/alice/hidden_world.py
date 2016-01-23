from itertools import zip_longest


def checkio(text, word):
    l = [list(i) for i in text.lower().replace(" ", "").split("\n")]
    l1 = ["".join(i) for i in l]
    l2 = ["".join(i) for i in list(zip_longest(*l1, fillvalue='-'))]

    for x, y in enumerate(l2, start=1):
        if word in y:
            return [y.index(word) + 1, x, y.index(word) + len(word), x]

    for x, y in enumerate(l1, start=1):
        if word in y:
            return [x, y.index(word) + 1, x, y.index(word) + len(word)]
