def make_key(key):
    s = 'abcdefghijklmnopqrstuvwxyz0123456789'
    k = "".join(sorted(set(key), key=key.index))
    for i in s:
        if i not in key:
            k += i
    return [k[i:i + 6] for i in range(0, 36, 6)]


def split_message(message, mode=1):
    m = "".join(map(str.lower, filter(str.isalnum, message)))
    r = m[0]
    for i in range(1, len(m)):
        if r[-1] == m[i] and len(r) % 2:
            if r[-1] == "x":
                r += "z" + m[i]
            else:
                r += "x" + m[i]
        else:
            r += m[i]
    if len(r) % 2:
        if r.endswith("z"):
            r += "x"
        else:
            r += "z"
    if mode == 1:
        return [r[i:i + 2] for i in range(0, len(r), 2)]
    else:
        return [message[i:i + 2] for i in range(0, len(message), 2)]


def encode(message, key, mode=1):
    message = split_message(message, mode=mode)
    key = make_key(key)

    def convert(x, y):
        for i in range(6):
            if key[i].find(x) + 1:
                x1, x2 = i, key[i].find(x)
        for i in range(6):
            if key[i].find(y) + 1:
                y1, y2 = i, key[i].find(y)

        if x1 == y1:
            x, y = key[x1][(x2 + mode) % 6], key[y1][(y2 + mode) % 6]
        elif x2 == y2:
            x, y = key[(x1 + mode) % 6][x2], key[(y1 + mode) % 6][y2]
        else:
            x, y = key[x1][y2], key[y1][x2]
        return x + y

    return "".join([convert(i[0], i[1]) for i in message])


def decode(secret_message, key):
    return encode(secret_message, key, mode=-1)


print(encode("How are you?", "hello"))
print(decode("ea2imb1ht0", "hello"))
