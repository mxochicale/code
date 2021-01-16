def hello(name,loud=False):
	if loud:
		print('HELLO %s' % name.upper() )
	else:
		print('Hello %s' % name)


hello('Bob')
hello('Miguel', loud=True)
