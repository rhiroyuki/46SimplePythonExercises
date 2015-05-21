"""
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.
"""

def is_palindrome(string):
	reverseString = ''
	for letter in string:
		reverseString = ''.join([letter, reverseString])
	return string == reverseString

def is_palindrome2(string):
	return string == string[::-1]


if __name__ == '__main__':
	print(is_palindrome('abacate'))
	print(is_palindrome('radar'))