"""
Write a function char_freq() that takes a string and builds a frequency 
listing of the characters contained in it. 
Represent the frequency listing as a Python dictionary. 
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
"""

import string
import testModule

def char_freq(phrase):
	phrase = phrase.lower()
	frequency = {key: phrase.count(key) for key in string.ascii_lowercase if phrase.count(key)!=0}
	f_list = [(key, value) for (key, value) in frequency.items()]
	print(sorted(f_list,key=lambda x: x[0]))
	return 0

if __name__ == '__main__':
	print(char_freq("abceda"))