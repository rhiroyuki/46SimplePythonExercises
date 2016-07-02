from colorama import init, Fore

class UnitTester(object):
	"""Class created to test functions"""
	def __init__(self):
		self.testes = 0

	def do_test(self, value, expected):
		init() 	# Windows compatibility with colored words
		self.testes += 1
		if value == expected:
			print(Fore.GREEN + 'Test %d PASSED!' %self.testes)
		else:
			print(Fore.RED + 'Test', self.testes,'ERROR!', Fore.RESET + 'Expected: "', expected,'" and Found: "', value, '"')

