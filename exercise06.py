"""
Define a function sum() and a function multiply()
that sums and multiplies (respectively)
all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4]) should return 10,
and multiply([1, 2, 3, 4]) should return 24.
"""


def sum(numberList):
    sum = 0
    for number in numberList:
        sum += number
    return sum


def multiply(numberList):
    mult = 1
    for number in numberList:
        mult *= number
    return mult

if __name__ == '__main__':
    print(sum([1, 2, 3, 4]))
    print(multiply([1, 2, 3, 4]))
