#first_last6
#Given an array of ints, returns True if 6 appears 
#as either the first or at last element in the array. 
#The array will be length 1 or more.
#

def fl(x):
	fe=x[0]
	le=x[len(x)-1]

	if fe==6  or le==6:
		return(True)

	return(False)
	#print( fe, le)

def main():
	x=[1,3,4,6]
	print ( fl(x)  )

	x=[6,3,4,1]
	print ( fl(x)  )

	x=[1,3,4,1]
	print ( fl(x)  )


if __name__=='__main__':
	main()
