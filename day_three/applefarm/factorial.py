def factorial(number):
	if number <= 1:
		return 1
	else:
		return number*factioral(number-1)


def fib(number):
	if number <= 1:
		return 1
	else:
		return fib(number-1) + fib(number-2)
		


for x in range(200):
	print(fib(x))