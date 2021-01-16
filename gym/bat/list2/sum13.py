#sum13.py
#
#Return the sum of numbers in the array,
#returning 0 for an empty array.
#Except the number 13 is very unlucky,
#so it does not count and numbers that come
#immediately after a 13 also do not count.
#



def s(x):
	N=len(x)
	if N==0:
		return(0)
	else:
		for i in range(0,N):
			if x[i]==13:
				i13=i

		s=0
		i=0
		while i<i13:
			s=s+x[i]
			i=i+1
	
	return ( s )
			

				
	
def main():
	print(s( []  ))
	print(s( [1,2,3,13,3]  ))
	print(s( [1,2,2,1,13,3]  ))
	print(s( [1,2,2,1,13]  ))

if __name__=='__main__':
	main()


