#How to add a border (filled with 0') around
#an existing array?

import numpy as np

def main():
	z=np.ones((5,5))
	z=np.pad(z, pad_width=1, mode='constant', constant_values=0)
	print(z)

if __name__=='__main__':
	main()
