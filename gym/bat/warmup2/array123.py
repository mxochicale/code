#array123
#Given an array of ints, return True if the sequence of numbers 1,2,3 appears
#in the array somewhere



def a0(a):
	a3=[1,2,3]
	for i in range( len(a)-2  ):
		a2= a[i:i+3] 
		if a2==a3:
			return(True)
	return(False)


def slt(nums):
	for i in range(len(nums)-2):
		if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
			return True
	return False

def main():
	a=[1,2,3,4,5]
	print( a0(a) )
	print( slt(a) )

	a=[1,1,3,4,5]
	print( a0(a) )
	print( slt(a) )
	
	a=[1,1,2,3,5]
	print( a0(a) )
	print( slt(a) )


if __name__=='__main__':
	main()




