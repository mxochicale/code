#create a random vector of size 30
#and find the mean value

import numpy as np

def main():
	z=np.random.random(30)
	print(z)
	m=z.mean()
	print(m)

if __name__=='__main__':
	main()
