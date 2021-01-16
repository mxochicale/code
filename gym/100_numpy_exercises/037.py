# 37	Create a 5x5 matrix with row values ranging 
#	from 0 to 4
	
import numpy as np

def main():
	z=np.zeros((5,5))	
	z+=np.arange(5)
	print(z)
		

if __name__=='__main__':
	main()
