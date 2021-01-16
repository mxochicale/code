def fib(n):
	"""Print Fibonacci series up to n"""
	a, b =0,1
	while a<n:
		print(a, end=' ')
		a, b = b, a+b
	print()



fib(4)
