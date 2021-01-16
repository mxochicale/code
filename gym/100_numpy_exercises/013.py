#Create a 10x10 array with random values
#and find the minimum and maximum values

import numpy as np
def main():
	z=np.random.random((10,10))
	print(z)
	zmin, zmax = z.min(), z.max()
	print(zmin, zmax)

if __name__=='__main__':
	main()
