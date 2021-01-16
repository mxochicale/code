# 43	Make an array immutable (read-only)


import numpy as np


def main():
	z=np.zeros(10)
	print(z)
	z.flags.writeable=False
	#z[0]=1
	print(z)
	

if __name__=='__main__':
	main()
