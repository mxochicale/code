def bubble(A,n):
	#print(A)
	#print(n)
	
	for k in range(0,n):
		print('k:',k)
		for i in range(0, n-k-1):
			print('  i:',i)
			#print(A[i])
			if (A[i]>A[i+1]):
				#print(A[i])
				temp=A[i]
				A[i]=A[i+1]
				A[i+1]=temp


	return(A)

def main():
	A = [7,4,5,2,1]
	n=5
	print( bubble(A,n)  )
	
	
	
if __name__=='__main__':
	main()
