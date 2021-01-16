#reverse3.py
#Given an array of ints lenght 3,
#return a new array with the elements 
#in reverse order, so [1,2,3]
#become [3,2,1]

def r3(x):
	return( [x[2], x[1], x[0]] )

def main():
	x=[3,2,1]
	print(	r3(x) )
	x=[7,0,-0]
	print(	r3(x) )


if __name__=='__main__':
	main()
