# 42	Consider two random array A and B,
#	check if they are equal.	


import numpy as np

def main():
	A= np.random.randint(0,2,5)
	print(A)
	B= np.random.randint(0,2,5)
	print(B)

	# Assuming identical shape of the arrays
	# and a tolerance for the comparison
	# of values 
	equal=np.allclose(A,B)
	print(equal)

	# Checking both the shape and the element
	# values, no tolerance 
	# (values have to be exactly equal)
	equal=np.array_equal(A,B)
	print(equal)




	

if __name__=='__main__':
	main()
