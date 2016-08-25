"""
Write a version of a palindrome recognizer that also accepts phrase palindromes
such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?",
"Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil",
"Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir",
or the exclamation "Dammit, I'm mad!".
Note that punctuation, capitalization, and spacing are usually ignored.
"""
import string


def remove_punctuation(phrase):
    stringAux = ''
    for eachChar in phrase:
        if eachChar not in string.punctuation:
            stringAux += eachChar
    return stringAux


def remove_whitespace(phrase):
    stringAux = phrase.lower().split()
    stringAux2 = ''
    for Word in stringAux:
        for eachChar in Word:
            stringAux2 += eachChar
    return stringAux2


def is_palindrome(phrase):
    stringAux = remove_punctuation(remove_whitespace(phrase))
    if stringAux == stringAux[::-1]:
        return True


if __name__ == '__main__':
    print (remove_punctuation(',lol,         '))
    print(remove_whitespace('lol , lol ,lol'))
    print(is_palindrome("Go hang a salami I'm a lasagna hog."))
