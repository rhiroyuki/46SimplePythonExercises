"""
Define a function that computes the length of a given list or string. 
(It is true that Python has the len() function built in, but writing 
it yourself is nevertheless a good exercise.)
"""
def listlen2(list):
	a = 0
	for i in list:
		a += 1
	return a

def counter(elementOfList):
	return 1

def listlen3(list):
	return sum(map(counter, list))

def listlen4(list):
	#replacing counter function with lambda function
	return sum(map(lambda x: 1,list))

def listlen6(list):
	#using list comprehension
	return sum([1 for i in list])

def listlen(list):
	#using generator expressions
	return sum((1 for i in list))


#tests
if __name__ == "__main__":
	print(listlen([1,2,3,4,5,6,7,8]))
	print(listlen('Banana'))
