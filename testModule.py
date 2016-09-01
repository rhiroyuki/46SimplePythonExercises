from colorama import init, Fore, Style
import time

class UnitTester(object):
	"""Class created to test functions"""
	def __init__(self):
		self.testes = 0

	def do_test(self, func, value, expected):
		init() 	# Windows compatibility with colored words
		self.testes += 1

		timeInit = time.time()
		result = func(value)
		if result == expected:
			print(Fore.GREEN + 'Test %d PASSED!' %(self.testes), Fore.RESET + \
					'Time:%.1fs' %(time.time()-timeInit))
		else:
			print(Fore.RED + 'Test', self.testes,'ERROR!', Fore.RESET + \
					'Expected: "', expected,'" and Found: "', result, '"')
		Style.RESET_ALL # Reset word colors

# Testing the test module

def test_timer(t):
	time.sleep(t)
	return t*t

if __name__ == '__main__':
	t1 = UnitTester()
	t1.do_test(test_timer, 1, 1)
	t1.do_test(test_timer, 2, 4)
	t1.do_test(test_timer, 3, 9)
	t1.do_test(test_timer, 4, 16)
