#left2.py
#Given a string, return a 'rotated left 2' version 
#where the first 2 chars are moved to the end.
#The string length will be at least 2.


def l(x):
	lx=len(x)
	if lx>1:
		l2=x[-2:]
		lr=x[0:-2]
		return(l2+lr)

	return('must be greater at least 2 lenght')

def main():
	x='coding'
	print(	l(x)  )
	x='Hello'
	print(	l(x)  )

	x='e'
	print(	l(x)  )



if __name__=='__main__':
	main()
