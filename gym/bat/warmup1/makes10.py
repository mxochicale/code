#Given 2 ints, a and b,
#return True if one of them is 10 
#or if theri sum is 10.



def mt0(a,b):
	if (a==10 or b==10 or  ((a+b)==10)   ):
		return(True)
	return(False)

def sol(a,b):
	return( a==10 or b==10 or a+b==10 )


def main():
	print(mt0(10,0)	)
	print(mt0(0,10)	)
	print(mt0(4,6)	)
	print(mt0(4,3)	)
	print(mt0(1,1)	)

	print(sol(10,0)	)
	print(sol(0,10)	)
	print(sol(4,6)	)
	print(sol(4,3)	)
	print(sol(1,1)	)


if __name__=='__main__':
	main()

