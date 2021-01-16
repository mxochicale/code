

def reverse(A):
	n=len(A)
	for i in range(n//2):
		other=n-i-1
		temp=A[i]
		A[i]=A[other]
		A[other]=temp

	return(A)	

def main():
	array=[1,1,2]
	rA=reverse(array)
	print(rA)


if __name__=='__main__':
	main()

