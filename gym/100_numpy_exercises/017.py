# What is the result of the following expression?

import numpy as np

def main():
	print( 0* np.nan )	
	print( np.nan == np.nan  )
	print( np.inf > np.nan )
	print( np.nan - np.nan )
	print(0.3 == 3*0.1)


if __name__=='__main__':
	main()
