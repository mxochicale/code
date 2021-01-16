# what are the results of the following expressions?

import numpy as np
def main():
	print(np.array(0) / np.array(0))
	print(np.array(0) // np.array(0))
	print(  np.array( [np.nan]  ).astype(int).astype(float)  )
	

if __name__=='__main__':
	main()
