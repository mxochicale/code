#How to find the memory size of any array

import numpy as np

def main():
	Z=np.zeros((10,10))
	print(Z)
	print( Z.size  )
	print( Z.itemsize )
	print("%d bytes" % (Z.size * Z.itemsize) )

if __name__=='__main__':
	main()



