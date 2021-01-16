##pos_neg.py
#Given 2 int values, return True if one is negative
#and one is posiive, Except if the parameter
#"negative" is True then return Ture if both are negative
#

def pn0(a,b,n):
	if ( a < 0 and b > 0 and n==False):
		return(True)
	elif (  a > 0 and b < 0 and n==False):
		return(True)		
	elif (a < 0 and b < 0 and n==True):
		return(True)
	return(False)	


def sol(a,b,n):
	if n:
		return(a<0 and b<0)
	else:
		return( (a<0 and b>0) or (a>0 and b<0)  )

def main():
	print( pn0(-1,1,False)	)
	print( pn0(1,-1,False)	)
	print( pn0(-1,-1,False)	)
	print( pn0(-1,-1,True)	)

	print( sol(-1,1,False)	)
	print( sol(1,-1,False)	)
	print( sol(-1,-1,False)	)
	print( sol(-1,-1,True)	)


if __name__ == '__main__':
	main()


