#without_end py
#Guven a string, return a version without 
#the first and last char, so 'Hello' yields 'ell'.
#The string length will be at least 2
#
def we(x):
	lx=len(x)

	if lx==2:
		return(x)			
	elif lx==3:
		return(x[0]+x[2])	
	elif lx>3:
		return(x[1:-1])
	return('char must be at least 2 lenght')

def main():
	x='c'
	print ( we(x)  )

	x='co'
	print ( we(x)  )

	x='cod'
	print ( we(x)  )

	x='coding'
	print ( we(x)  )


if __name__=='__main__':
	main()

