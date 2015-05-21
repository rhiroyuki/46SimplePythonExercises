"""
Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".
"""

def reverse2(string):
	return string[::-1]

def reverse(string):
	#is list comprehension possible?
	reversed = ''
	for letter in string:
		reversed = ''.join([letter, reversed])
	return reversed

if __name__ == '__main__':
	print(reverse('I am testing'))