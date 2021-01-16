#create a 2nd array with 1 on the border and 0 inside

import numpy as np
def main():
	z=np.ones((10,10))
	z[1:-1,1:-1]=0
	print(z)

if __name__=='__main__':
	main()
