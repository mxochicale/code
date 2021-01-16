# 44 Consider a random 10x2 matrix
#	representing cartesian coordinates,
#	convert them to polar coordinates


import numpy as np

def main():
	z=np.random.random((10,2))
	x,y=z[:,0], z[:,1]
	R=np.sqrt(x**2+y**2)	
	T=np.arctan2(y,x)
	print(R)
	print(T)


if __name__=='__main__':
	main()
