#array_front9
#Given an array of ints, 
#return True if one of the first 4 elements
#in the array is a 9. 
#The array length may be less than 4
#


def af0(a):
	n=len(a)

	if n<=4:
		for i in range(n):
			if a[i]==9:
				return(True)
	return(False)


def slt(a):
	end=len(a)
	if end > 4:
		end=4
	
	for i in range(end):
		if a[i]==9:
			return True
	return False

def main():
	a=[1,2,4]
	print(	af0(a) )
	a=[1,2,9,4]
	print(	af0(a) )
	a=[1,2,0,4,9]
	print(	af0(a) )

	a=[1,2,4]
	print(	slt(a) )
	a=[1,2,9,4]
	print(	slt(a) )
	a=[1,2,0,4,9]
	print(	slt(a) )





if __name__=='__main__':
	main()

