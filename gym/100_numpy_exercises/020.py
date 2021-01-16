# Consider a (6,7,8) shape array, 
# what is the index (x,y,z) of the 100th element?


import numpy as np

def main():
	z=np.unravel_index(99, (6,7,8))
	#z=np.unravel_index(3, (3,3))
	print(z)	

if __name__=='__main__':
	main()

