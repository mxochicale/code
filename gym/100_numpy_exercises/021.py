# Create a checkboard 8x8 matrix using
# the tile function.

import numpy as np
def main():
	z=np.tile( np.array([[0,1],[1,0]]),(4,4)  )
	print(z)

if __name__=='__main__':
	main()
