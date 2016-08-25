"""
Write a function is_member() that takes a value (i.e. a number, string, etc)
x and a list of values a, and returns True if x is a member of a,
False otherwise.
(Note that this is exactly what the in operator does,
but for the sake of the exercise you should
pretend Python did not have this operator.)
"""


def is_member6(elementX, listA):
    if(list(map(lambda x: elementX == x, listA))):
        return True
    return False


def is_member4(elementX, listA):
    for element in listA:
        if (element == elementX):
            return True
    return False


def is_member3(elementX, listA):
    # return true if the list made by list comprehesion is not empty
    if ([True for element in listA if element == elementX]):
        return True
    return False


def is_member(elementX, listA):
    return elementX in listA

if __name__ == '__main__':
    print(is_member(3, [1, 2, 3]))
    print(is_member(4, [1, 2, 3]))
    print(is_member('a', 'ABRA'))
    print(is_member('a', 'abra'))
    print(is_member('a', 'b'))
