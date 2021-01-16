#close_far.py
#Given three ints, abc, return True if one 
#of b or c is 'close' (differing from a by at most 1),
#while the other is "far", differing from both other values by 2 or more.
#Note: abs(num) computes the absolute value of a number.
#

def cf0(a,b,c):
	if abs(a-b)==1 and abs(a-c)>=2:
		return(True)
	if abs(a-b)>=2 and abs(a-c)==1:
		return(True)
	return(False)

def cf1(a,b,c):
	if abs(a-b)==1:
		if abs(c-a)>=2 and abs(c-b)>=2:
			return(True)		
	if abs(a-c)==1:
		if abs(b-a)>=2 and abs(b-c)>=2:
			return(True)		
	return(False)

def main():
	print( cf1(1,2,10)  ) #True
	print( cf1(1,2,3)  ) #False
	print( cf1(4,1,3)  ) #True

if __name__=='__main__':
	main()

