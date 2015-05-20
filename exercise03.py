"""
Define a function that computes the length of a given list or string. 
(It is true that Python has the len() function built in, but writing 
it yourself is nevertheless a good exercise.)
"""
#Is there a way to do it without iterating?
def counter(elementOfList):
	return 1

def listlen3(list):
	return sum(map(counter, list))

def listlen(list):
	#replacing counter function with a lambda function
	return sum(map(lambda x: 1,list))

def listlen2(list):
	a = 0
	for i in list:
		a += 1
	return a

#tests
if __name__ == "__main__":
	print(listlen([1,2,3,4,5,6,7,8]))
	print(listlen('Banana'))
