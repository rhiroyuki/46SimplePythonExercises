"""
Define a function overlapping() that takes two lists and returns True
if they have at least one member in common, False otherwise.
You may use your is_member() function, or the in operator,
but for the sake of the exercise, you should (also)
write it using two nested for-loops.
"""
from exercise09 import is_member


def overlapping(listA, listB):
    # Is there a simple way to do it?
    for elementA in listA:
        if(is_member(elementA, listB)):
            return True
    return False


def overlapping2(listA, listB):
    for elementA in listA:
        for elementB in listB:
            if elementB == elementA:
                return True
    return False


if __name__ == '__main__':
    print(overlapping([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
    print(overlapping([1, 2, 3, 4, 5], [0]))
