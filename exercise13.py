"""
The function max() from exercise 1) and the function max_of_three()
from exercise 2) will only work for two and three numbers, respectively.
But suppose we have a much larger number of numbers,
or suppose we cannot tell in advance how many they are?
Write a function max_in_list() that takes
a list of numbers and returns the largest one.

"""


def max_in_list(numberList):
    bigNumber = numberList[0]
    for number in numberList:
        if number > bigNumber:
            bigNumber = number
    return bigNumber


def max_in_list2(numberList):
    a = sorted(numberList)[-1]
    return a


def max_in_list3(numberList):
    return max(numberList)

if __name__ == '__main__':
    print(max_in_list([1, 2, 10, 3]))
    print(max_in_list([1, 19, 78, 3]))
    print(max_in_list([-1, -19, -78, -3]))
