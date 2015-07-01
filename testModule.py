class UnitTester(object):
	"""Class created to test functions"""
	def __init__(self):
		self.testes = 0

	def do_test(self, value, expected):
		self.testes += 1
		if value == expected:
			print('Test %d passed!' %self.testes)
		else:
			print('Test', self.testes,'Error, expected', expected,'found:', value)

#def soma(a, b):
#	return a+b

#def reversedList(lista):
#	return lista[::-1]

#soma(1,2,3)
#teste = UnitTester()
#teste.test(soma(1,2), 3)
#teste.test(soma(3,5), 8)
#teste.test(soma(1,2), 0)
#teste.test(soma(1,2), 3)
#teste.test(soma(1,3), 3)
#teste.test(soma(1,5), 3)

#teste2 = UnitTester()
#teste2.test(reversedList('abacate'), 'etacaba')
#teste2.test(reversedList([1,2,3,45,321,6]), [6, 321, 45, 3, 2, 1])