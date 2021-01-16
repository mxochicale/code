#first_half.py
#Given a string of even lenght, return the first half.
#So the string "WooHoo", yiedls "Woo"
#


def fh(x):
	lx=int( len(x)/2 )
	return( x[:lx] )

def main():
	x='WooHoo'
	print( fh(x) )
	x='WooHoodd'
	print( fh(x) )


if __name__=='__main__':
	main()

