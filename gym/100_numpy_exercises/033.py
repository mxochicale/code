#How to get the dates of yesterday, today and tomorrow?

import numpy as np
def main():
	yesterday=np.datetime64('today', 'D') - np.timedelta64(1,'D')
	print( yesterday )

	today=np.datetime64('today', 'D') 
	print( today )
	
	tomorrow=np.datetime64('today', 'D') + np.timedelta64(1,'D')
	print( tomorrow )

if __name__=='__main__':
	main()

