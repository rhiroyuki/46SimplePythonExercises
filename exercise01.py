def max(number1, number2):
	if number1 > number2:
		return number1
	else:
		return number2;

#some tests
if __name__ == "__main__":
	print(max(2, 3))
	print(max(3, 2))
	print(max(3.2, 2.3))
	print(max(2.3, 3.2))