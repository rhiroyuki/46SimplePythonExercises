
"""
Write a function that takes a character (i.e. a string of length 1) 
and returns True if it is a vowel, False otherwise.
"""

def isVowel(character):
	return character in 'aeiou'

def isVowel2(character):
	if character in 'aeiou':
		return True
	else:
		return False

#tests
if __name__ == "__main__":
	print(isVowel('a'))
	print(isVowel('b'))
