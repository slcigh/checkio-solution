def convert(n, d):
    fraction_digits = []
    repeating_at = 0
    rem = (n % d) * 10
    remainders = []
    whole = int(n/d)

    while not repeating_at:
        remainders.append(rem)
        digit = int(rem / d)
        if rem != 0:
            fraction_digits.append(str(digit))
        rem = (rem % d) * 10
        if rem in remainders:
            repeating_at = remainders.index(rem)+1

    pos = repeating_at - 1
    before_pos = "".join(fraction_digits)[:pos]
    if "".join(fraction_digits)[pos:]:
        after_pos = "(" + "".join(fraction_digits)[pos:] + ")"
    else:
        after_pos = ""

    return str(whole) + "." + before_pos + after_pos
