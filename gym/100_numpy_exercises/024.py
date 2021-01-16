#Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
import numpy as np
def main():
	#z= np.dot ( np.ones((5,3)), np.ones((3,2)) )
	z= np.dot ( np.ones((5,4)), np.ones((4,6)) )
	print(z)

if __name__=='__main__':
	main()
