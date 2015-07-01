"""
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
"""

text = """The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers.
The Python Software Foundation (PSF) is a non-profit membership organization devoted to advancing open source technology related to the Python programming language. It qualifies under the US Internal Revenue Code as a tax-exempt 501(c)(3) scientific and educational public charity, and conducts its business according to the rules for such organizations.
"""
text = text.split()
wordCounter = {word: len(word) for word in text}

#for word in text:
#	if word not in wordCounter:
#		wordCounter[word] = len(word)

print(wordCounter)
