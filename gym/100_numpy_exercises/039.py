# 39	Create a vector of size 10 with values
# 	ranging from 0 to 1, both excluded.

import numpy as np

def main():
	z=np.linspace(0,1,11,endpoint=False)[1:]
	print(z)

if __name__=='__main__':
	main()
