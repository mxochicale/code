#array_count9.py
#Given an array of ints,
#return the number of 9's in the array
#

def ac0(a):
	
	c=0
	for i in range(len(a)):
		if a[i]==9:	
			c=c+1
	return(c)


def slt(a):
	count=0
	for num in a:
		if num == 9:
			count=count+1
	return(count)
	

def main():
	a=[1,2,3,9]
	print (  ac0(a) )
	print (  slt(a) )

	a=[1,9,9,9]
	print (  ac0(a) )
	print (  slt(a) )

if __name__=='__main__':
	main()


