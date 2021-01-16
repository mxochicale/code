# Create a 5x5 matrix with values 1,2,3,4 just below the diagonal


import numpy as np

def main():
	z=np.diag(1+np.arange(4),k=-1)
	#z=np.diag(1+np.arange(4))
	#z=np.diag(np.arange(4))
	print(z)
	

if __name__=='__main__':
	main()
