# 46 	Create a structured array with x and y
# 	coordinates covering the 
#	\[0,1\]x\[0,1\] area


import numpy as np

def main():
	z=np.zeros( (5,5),  [('x', float),('y',float) ] )
	z['x'],z['y']=np.meshgrid(
				np.linspace(0,1,5),
				np.linspace(0,1,5)
				)
		
	print(z)

	

if __name__=='__main__':
	main()
