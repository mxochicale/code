#count_events.py
#
#Return the number of even ints in the given array.
#Note: the % 'mod' operator computes the remainder,
#e.g. 5%2 1
#

def ce(x):
	ne=0
	for i in range(0, len(x)):
		#print(x[i]%2)
		if x[i]%2 == 0:
			ne=ne+1
	return(ne)

def main():
	print( ce(  [2,1,2,3,4]  )  )
	print( ce(  [2,2,0]  )  )
	print( ce(  [1,3,5]  )  )

if __name__=='__main__':
	main()

