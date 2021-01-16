#make_abba.py
#Given two strings, a and b, 
#return the result of putting them together in the order
#abba, e.g. "Hi" and "Bye"
#returns "HiByeByeHi"
#


def ma0(a,b):
	return(a+b+b+a)

def main():
	a='Hi'
	b='Bye'
	print ( ma0(a,b) )

if __name__=='__main__':
	main()


