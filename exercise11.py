"""
Define a function generate_n_chars() that takes an integer n and a character c and returns a string, 
n characters long, consisting only of c:s. 
For example, generate_n_chars(5,"x") should return the string "xxxxx". 
(Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". 
For the sake of the exercise you should ignore that the problem can be solved in this manner.)
"""
def generate_n_chars(n, c):
	a = []
	for useless in range(n):
		a.append(c)
	return ''.join(a)

def generate_n_chars4(n, c):
	a = ''
	for useless in range(n):
		a += c
	return a

def generate_n_chars2(n, c):
	return ''.join([c for nothing in range(n)])

def generate_n_chars3(n, c):
	return c*n

if __name__ == '__main__':
	print(generate_n_chars(4,'b') == 'bbbb')
	print(generate_n_chars(2,'A') == 'AA')
