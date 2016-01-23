def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1) * word.isalpha()
        if succ == 3:
            return True
    else:
        return False


"""
import re
def checkio(words):
    return bool(re.compile("([a-zA-Z]+ ){2}[a-zA-Z]+").search(words))
   # or re.sub(r'\D+ \D+ \D+','',w)!=w
"""

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
