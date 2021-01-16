#max_end3.py
#Given an array of ints length 3, figure out 
#which is the larger, the first or last element in the array,
#and set all the other elements to be that value.
#Return the changed array.

def me(x):
	if x[0]>x[2]:
		return( [x[0], x[0], x[0]] )
	elif x[2]>x[0]:
		return( [x[2], x[2], x[2]] )

	return(x)

def main():
	x=[1,3,4]
	print(  me(x) )
	x=[6,3,4]
	print(  me(x) )


if __name__=='__main__':
	main()

