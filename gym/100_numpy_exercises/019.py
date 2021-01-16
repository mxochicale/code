# Create a 8x8 matrix and fill it with 
# a checkboard pattern
import numpy as np

def main():
	z=np.zeros((8,8),dtype=int)
	z[1::2,::2]=1
	z[::2,1::2]=1
	print(z)	

if __name__=='__main__':
	main()
