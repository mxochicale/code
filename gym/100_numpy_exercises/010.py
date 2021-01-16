# Find indices of non-zero elements from [1,2,0,0,4,0]

import numpy as np
def main():
	nz=np.nonzero([1,2,0,0,4,0])
	print(nz)

if __name__=='__main__':
	main()
