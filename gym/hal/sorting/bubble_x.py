# bubble algorithm

def bubble(X):
	n=len(X)	
	#print(n)
	for k in range(0,n):
		#print(X[k])
		print('k:',k)
	
		for i in range(0, n-k-1  ):
			print('  i:',i)		
			print('  X[i]:',X[i])		
			if (X[i] > X[i+1]):
				temp=X[i]
				#print('temp',temp)
				X[i]=X[i+1]
				X[i+1]=temp


	print(X)

def main():
	A=[5,1,3,2,6]
	bubble(A)


if __name__=='__main__':
	main()



