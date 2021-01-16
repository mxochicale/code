#lone_sum.py
#Given 3 int values a,b,c return their sum.
#However, if one of the values is the same
#as another of the values, it does not count
#toward the sum
#

def s0(a,b,c):
	if a!=b and b!=c and a!=c:
		s=a+b+c
	elif a!=b and (c==a or c==b):
		s=a+b
	elif b!=c and (a==b or a==c):
		s=b+c
	elif a!=c and (b==a or b==c):
		s=a+c
	else:
		s=0
	return(s)


def s1(a,b,c):
	if a!=b and b!=c and a!=c:
		s=a+b+c
	elif a!=b and c==a:
		s=b
	elif a!=b and b==c:
		s=a
	elif b!=c and a==b:
		s=c
#	elif b!=c and a==b:
#		s=c
	elif a==b and b==c:
		s=0
	else:
		s=0
	return(s)



def main():
	#print( s0(1,2,3) )
	#print( s0(3,2,3) )
	#print( s0(3,3,3) )

	print( s1(1,2,3) )
	print( s1(3,2,3) )
	print( s1(3,3,2) )
	print( s1(3,3,3) )


if __name__=='__main__':
	main()

