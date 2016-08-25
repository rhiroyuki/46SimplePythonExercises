"""
Write a function find_longest_word() that takes a
list of words and returns the length of the longest one.
"""
from testModule import UnitTester


def find_longest_word(wordList):
    biggerLength = 0
    for word in wordList:
        if len(word) > biggerLength:
            biggerLength = len(word)
    return biggerLength

if __name__ == '__main__':
    teste = UnitTester()
    teste.do_test(find_longest_word(['abacaxi', 'arara', 'aracaju', 'joão', 'brasilia']), 8)
    teste.do_test(find_longest_word(['abacaxi', 'arara', 'aracaju12333', 'joão', 'brasilia']), 12)
    teste.do_test(find_longest_word(['abacaxi', 'arara', 'aracaju321', 'joão', 'brasilia']), 10)
