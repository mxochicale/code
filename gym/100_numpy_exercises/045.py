# 45 	Create random vector of size 10 and
#	replace the maximum value by 0


import numpy as np

def main():
	z=np.random.random(10)
	z[z.argmax()]=0
	print(z)


if __name__=='__main__':
	main()
