#lucky_sum.py
#Given 3 int values, a,b,c, return their sum.
#However, if one of the values is 13,
#then it does not count towards the sum 
#and values to its right does not count.
#For example, if b is 13,
#then both b and c
#do not count.
#

def s0(a,b,c):
	t=13
	
	if a!=t and b!=t and c!=t:
		s=a+b+c
	if c==t:
		s=a+b
	if b==t:
		s=a
	if a==t:
		s=0
	return(s)


def main():
	print( s0(1,2,3) )
	print( s0(1,2,13) )
	print( s0(1,13,1) )

if __name__=='__main__':
	main()

