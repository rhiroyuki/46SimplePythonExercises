"""
Define a function max_of_three() that takes three numbers
as arguments and returns the largest of them.
"""


def max_of_three3(number1, number2, number3):
    return sorted([number1, number2, number3])[-1]


def max_of_three2(number1, number2, number3):
    return max([number1, number2, number3])


def max_of_three(number1, number2, number3):
    if number1 > number2:
        if number1 > number3:
            return number1
        else:
            return number3
    else:
        if number2 > number3:
            return number2
        else:
            return number3


print(max_of_three(1, 2, 3))
print(max_of_three(2, 2, 2))
print(max_of_three(2, 2, 3))
print(max_of_three(2, 3, 2))
print(max_of_three(3, 2, 2))
