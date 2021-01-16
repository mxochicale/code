#Create a custom dtype that describes
#a color as four unsigned bytes (RGBA)

import numpy as np
def main():
	colour=	np.dtype([	('r', np.ubyte,1),
				('g', np.ubyte,1),
				('b', np.ubyte,1),
				('a', np.ubyte,1)
			])
	print( colour )

if __name__=='__main__':
	main()

