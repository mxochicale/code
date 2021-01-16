#non_start.py
#Given 2 string, return their concatenation, expept omit
#the first char of each.
#The string will be at least lenght 1
#

def ns(a,b):	
	print( len(a)>1 & len(b)>1)
	print( len(a)>1 and len(b)>1)
	
	if len(a)>1 and len(b)>1:
		return( a[1:]+b[1:] )
	return('len must be >1')
	
def main():
	a='coding'
	b='super'
	print ( ns(a,b) )

	a='c'
	b='super'
	print ( ns(a,b) )


if __name__=='__main__':
	main()

