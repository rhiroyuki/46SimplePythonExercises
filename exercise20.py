"""
Represent a small bilingual lexicon as a Python dictionary in the following fashion 
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} 
and use it to translate your Christmas cards from English into Swedish. 
That is, write a function translate() that takes a list of English words and returns a list of Swedish words.
"""

import testModule

def translate(phrase):
	translation = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
	listPhrase = phrase.lower().split()
	result = []
	for word in listPhrase:
		result.append(translation[word])
	return " ".join(result)

if __name__ == '__main__':
	test = testModule.UnitTester()
	test.do_test(translate("Merry Christmas"), "god jul");