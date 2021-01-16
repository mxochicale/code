#sum67.py
#Return the sum of the numbers in the array,
#except ignore sections of numbers starting with a 6
#and extending the next 7 (every 6 will be followed by at least one 7).
#Return 0 for no numbers.
#


def s(x):
	N=len(x)
	if N==0:
		return(0)
	else:
		for i in range(0,N):
			if x[i]==6:
				i6=i
			if x[i]==7:
				i7=i

		for k in range(i6,i7+1):
			x[k]=0

		s=0
		for j in range(0,N):
			s=s+x[j]

	return(s)

def main():
	#print(s([]))
	print(s([1,1,6,7,2]))
	print(s([6,1,7,1,1,2]))
	print(s([4,1,2,1,6,7]))
	print(s([1,2,2,6,99,99,7]))

if __name__=='__main__':
	main()


