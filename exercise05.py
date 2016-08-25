"""
Write a function translate() that will translate a text into "rövarspråket"
(Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun") should return the string
"tothohisos isos fofunon".
"""


def translate(string):
    # Is there a way to be more simple?
    return ''.join([''.join([letter, 'o', letter])
                    if letter not in 'ae iou'
                    else ''.join(letter) for letter in string])


def translate2(string):
    newString = ''
    for letter in string:
        if letter not in 'ae iou':
            newString += ''.join([letter, 'o', letter])
        else:
            newString += ''.join(letter)
        return newString


if __name__ == '__main__':
    print(translate('this is fun'))
