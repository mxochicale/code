#sum3.py
#Given an array of ints lenght 3,
#return the sum of all the elements


def s(x):	
	return(x[0]+x[1]+x[2])

def main():
	x=[1,2,3]
	print ( s(x) )
	x=[0,0,3]
	print ( s(x) )


if __name__=='__main__':
	main()
