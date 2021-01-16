#extra_end.py
#Given a string, return a new string made of 3 copies
#of the last 2 chars of the original string.
#The string length will be at least 2.


def ee0(x):

	if len(x)>=2:
		lt=x[-2:]
		return(lt+lt+lt)	
	return('string should be at least of a lenght of two')
	

def main():
	x='gan'
	print( ee0(x) )
	x='v'
	print( ee0(x) )
	x='Re'
	print( ee0(x) )


if __name__=='__main__':
	main()


