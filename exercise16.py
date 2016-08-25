"""
Write a function filter_long_words() that takes a list of words
and an integer n and returns the list of words that are longer than n.
"""
from testModule import UnitTester


def filter_long_words(wordList, intN):
    return [word for word in wordList if len(word) > intN]

if __name__ == '__main__':
    test = UnitTester()
    test.do_test(filter_long_words(['abacaxi', 'arara', 'aracaju', 'joão', 'brasilia', '7'], 6), ['abacaxi', 'aracaju', 'brasilia'])
