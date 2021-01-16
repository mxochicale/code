#How to round away from zero a float array?

import numpy as np
def main():
	z=np.random.uniform(-10,10,10)
	print(z)
	print( np.copysign(np.ceil( np.abs(z)), z , z)  )

if __name__ == '__main__':
	main()
