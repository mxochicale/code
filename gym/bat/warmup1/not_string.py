
#Given a string, return a new string where "not" has been added
#to the front. However, if the string already begins with "not",
#return the string unchanged.


def ns0(x):
	lx=len(x)
	isnot = x[:3]
	if isnot=='not':	
		return( x[:lx] )
	return ('not'+x)


def slt(str):
	if len(str)>=3 and str[:3]=='not':
		return str
	return 'not '+str



def main():
	s='not is not'
	print( ns0(s) )
	s='no is not'
	print( ns0(s) )

	s='not is not'
	print( slt(s) )
	s='no is not'
	print( slt(s) )







if __name__=='__main__':
	main()



