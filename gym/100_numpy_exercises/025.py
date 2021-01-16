#Given a 1D array, negate all elements 
#which are between 3 and 8, in place.

import numpy as np
def main():
	z=np.arange(11)
	z[(3<z)&(z<=8)] *=-1
	print(z)

if __name__=='__main__':
	main()

