"""
A pangram is a sentence that contains all the letters of the English alphabet at least once, 
for example: The quick brown fox jumps over the lazy dog. 
Your task here is to write a function to check a sentence to see if it is a pangram or not.
"""
import string
import testModule

def is_pangram(phrase):
	letterCount = {}
	for letter in phrase.lower():
		if letter in string.ascii_lowercase:
			letterCount[letter] = 1
	return len(letterCount) == len(string.ascii_lowercase)

if __name__ == '__main__':
	teste = testModule.UnitTester()
	teste.do_test(is_pangram("The quick brown fox jumps over the lazy dog"), True)
	teste.do_test(is_pangram("The quick brown fox jumps over the lazy d123125776!#!@$%^&&*8789dog"), True)
	teste.do_test(is_pangram(" "), False)
	teste.do_test(is_pangram("ta comigo pow"), False)
	teste.do_test(is_pangram(string.ascii_uppercase), True)
	teste.do_test(is_pangram(string.ascii_lowercase), True)