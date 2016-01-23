def checkio(n):
    return 'Fizz' * (not n % 3) + ' ' * (not n % 15) + 'Buzz' * (not n % 5) or str(n)


if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
