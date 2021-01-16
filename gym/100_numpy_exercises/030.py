# how to find common values between two arrays?

import numpy as np
def main():
	z1=np.random.randint(0,10,10)
	z2=np.random.randint(0,10,10)

	print(z1)
	print(z2)
	
	print(np.intersect1d(z1,z2))
	

if __name__=='__main__':
	main()
