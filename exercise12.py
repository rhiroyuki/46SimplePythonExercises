"""
Define a procedure histogram() that takes a list of integers and prints
a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:

****
*********
*******
"""


def histogram2(intList):
    for number in intList:
        print('*' * number)


if __name__ == '__main__':
    histogram([4, 9, 7])
