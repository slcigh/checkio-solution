from itertools import chain, cycle


def amsco(iterable, key):
    matrix, it, odd_row = [[_] for _ in str(key)], iter(iterable), 1
    print(matrix)
    print(list(chain([None], matrix)))
    try:
        for l in cycle(chain([None], matrix)):
            if l is None:
                one_two = odd_row = 3 - odd_row
            else:
                one_two = 3 - one_two
                for _ in range(one_two):
                    l.append(next(it))
    except StopIteration:
        print(matrix)
        return [_[1:] for _ in sorted(matrix)]

message = "oruoreemdstmioitlpslam"

print(list(amsco(range(len(message)), 4123)))