#same_first_last.py
#Given an array of ints, return True 
#if the array is length 1 or more, and the first element
#and the last element are equal.
#
def sfl(x):
	fe=x[0]
	le=x[len(x)-1]
	#print(fe, le)
	if fe==le and len(x)>1:
		return(True)
	return(False)


def main():
	x=[1,2,3,1]
	print( sfl(x) ) 

	x=[1,2,3,2]
	print( sfl(x) ) 

	x=[11]
	print( sfl(x) ) 

	x=[11,11]
	print( sfl(x) )



if __name__=='__main__':
	main()
