#round_sum.py
#For this problem,  we will round and int value up
#to the next multiple of 10 if its rightmost digit is 5 or more,
#so 15 rounds up to 20.
#Alternatively, round down to the previous multiple of 10,
#if its rightmost is less than 5, so 12 rounds down to 10.
#Given 3 ints, abc, return the sum of their rounded values.
#To avoid code repetition, write a separate helper
#"def_round10(n):" and calll it 3 times.
#Write the helper entirely below and at the same indent
#level as round_sum().
#

def rs(a,b,c):
	#print( r10(a) )	
	return(  r10(a)+r10(b)+r10(c) )

def r10(n):
	r=n%10
	if r>=5:
		return(n+(10-r) )
	if r<5:
		return( n-r )

def main():
	print(  rs(16,17,18) ) 
	print(  rs(12,13,14) ) 
	print(  rs(6,4,4) ) 

if __name__=='__main__':
	main()
