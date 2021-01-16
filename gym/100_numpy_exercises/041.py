# 41	How to sum a small array faster than 
# 	np.sum?

import numpy as np

def main():
	z=np.arange(10)
	s=np.add.reduce(z)
	print(s)


if __name__=='__main__':
	main()


