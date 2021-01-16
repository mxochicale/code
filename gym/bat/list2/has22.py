#has22.py
#Given an array of ints, return True if the array 
#contains a 2 next to a 2 somewhere.
#

def h(x):
	N=len(x)
	for i in range(0,N-1):
		#print( x[i], x[i+1] )
		if x[i]==2 and x[i+1]==2:
			return(True)
		#else:
	return(False)
		

def main():
	print (h([1,2,2]))
	print (h([1,2,1,2]))
	print (h([2,1,2]))

if __name__=='__main__':
	main()

