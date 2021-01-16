#no_teen_sum.py
#Given 3 int values, abc, return their sum.
#However if any of the values is a teen
#-- in the range 13..19 inclusive--
#then that value counts as 0, exept 15 and 16
#do not count as teens.
#Write a separate helper
#"def fix_teen(n):"  that takes in an int value
#and returns that value fixed for the teen rule.
#In this way, you avoid repeating the teen
#code 3 times (i.e 'decomposition').
#Define the helper below and at the same time 
#ident level as the main no_teen_sum().
#

def fixteen(n):
	if n>=13 and n<=19:
		if n==15 or n==16:
			return(n)
		return(0)
	else:
		return(n)
				

def nts(a,b,c):
	return( fixteen(a)+fixteen(b)+fixteen(c) )

def main():
	print (  nts(1,2,3) )
	print (  nts(2,13,1) )
	print (  nts(2,1,14) )

	#print (  nts(13,1,14) )
	#print (  nts(15,1,14) )
	#print (  nts(16,1,14) )
	#print (  nts(17,1,14) )

if __name__=='__main__':
	main()

