#rotate_left3.py
#Given an array of ints lenght 3,
#return an array with the elements 
#'rotated left' so [1,2,3] return [2,3,1]

def r(x):
	#le=x[len(x)-1]
	#print( x[0:2] , le )
	r= [ x[1], x[2], x[0] ] 

	return( r )

def main():
	x=[1,2,3]
	print(r(x))
	x=[5,11,9]
	print(r(x))


if __name__=='__main__':
	main()
