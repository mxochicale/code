# 47	Given two arrays, x and y,
# 	construct the cauchy matrix 
#	C( Cij = 1/(xi-yj)  )


import numpy as np

def main():
	x=np.arange(8)	
	y=x+0.5
	C=1.0 / np.subtract.outer(x,y)
	print(C)
	#print(np.lihalg.det(C))
	#print(x,y)

if __name__=='__main__':
	main()
