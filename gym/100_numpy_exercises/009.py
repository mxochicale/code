#create a 3x3 matrix with values ranging from 0 to 9
import numpy as np
def main():
	z=np.arange(9).reshape(3,3)
	print(z)

if __name__=='__main__':
	main()
