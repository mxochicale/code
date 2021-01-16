#sum2.py
#Given an array of ints, return the sum of the first 2 elements 
#in the array. If the array is less than 2, just sum up
#the elements that exist. returning 0 if the array is lenght 0
#


def s(x):
	if len(x)>=2:
		return ( x[0]+x[1] )
	return (0)


def main():
	x=[]
	print(s(x))
	x=[1,2]
	print(s(x))
	x=[2,3,1,23,2]
	print(s(x))



if __name__=='__main__':
	main()

