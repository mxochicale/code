#hello_name.py
#Given a string name, e.g. "Bob",
#return a greeting of the form: "Hello Bob!".
#




def hw0(x):
	n=x
	gn='Hello '+n+'!'	
	return(gn)

def slt(x):
	return( 'hello '+x  )




def main():
	x='Ricky'
	print(	hw0(x) )
	print(	slt(x) )

if __name__=='__main__':
	main()

