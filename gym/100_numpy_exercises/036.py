# 36 	Extract the integer part of a random array
# 	using 5 differenc methods

import numpy as np

def main():
	Z=np.random.uniform(0,10,10)
	print(Z)
	print(Z-Z%1)
	print(np.floor(Z))
	print(np.ceil(Z))
	print(Z.astype(int))
	print(np.trunc(Z))
		

if __name__=='__main__':
	main()
