#make_ends.py
#Given an array of ints, return a new array length 2
#containing the first and last elements from 
#the original array.
#The original array will be lenght of 1 or more.
#

def me(x):
	#print (len(x))
	if len(x)>1:
		return([  x[0], x[len(x)-1]  ]   )
	return('x must be greater than 1')


def main():
	x=[]
	print( me(x) )
	x=[1]
	print( me(x) )
	x=[1,2]
	print( me(x) )
	x=[1,2,3]
	print( me(x) )
	x=[1,2,3,4]
	print( me(x) )





if __name__=='__main__':
	main()
