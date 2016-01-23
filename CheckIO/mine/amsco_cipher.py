import re


def decode_amsco(message, key):
    length = int((len(message)+1)*2/3)
    width = len(str(key))
    height = int((length+width-1)/width)
    key = [str(key).index(str(i)) for i in range(1, width+1)]
    it = iter(message)
    r = [[1 for i in range(width)] for j in range(height)]

    if length % width:
        temp = width - (length % width)
        while temp:
            r[-1].pop()
            temp -= 1

    for i in range(0, height, 2):
        for j in range(1, width, 2):
            try:
                r[i][j] += 1
            except IndexError:
                pass

    for i in range(1, height, 2):
        for j in range(0, width, 2):
            try:
                r[i][j] += 1
            except IndexError:
                pass

    if sum([sum(i) for i in r]) > len(message):
        r[-1][-1] -= 1

    for col in key:
        for row in range(height):
            try:
                t = r[row][col]
                a = []
                while t:
                    a.append(it.__next__())
                    t -= 1
                r[row][col] = a
            except IndexError:
                pass
    return re.sub(r'[^\w+]', "", str(r))


print(decode_amsco("oruoreemdstmioitlpslam", 4123))
print(decode_amsco('kicheco', 23415))
print(decode_amsco('hrewhoorrowyilmmmoaouletow', 123))
print(decode_amsco(u"lsesanaeamiauelodosadonpieulneittgemtdsorstenomemalorccicegnsutadalirpmeritolomcoiengae", 654287931))