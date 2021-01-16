#How to get all the dates corresponding to 
#the month of July 2016?

import numpy as np

def main():
	z=np.arange('2016-07','2016-08', dtype='datetime64[D]')
	print(z)

if __name__=='__main__':
	main()
