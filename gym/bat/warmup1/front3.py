###front3
#Given a string, we will say that the front is the first 3 chars
#of the string. 
#If the string length is less than 3, the front is whatever is there.
#Return a new string which is 3 copies of the front.
#


def f0(s):
	if len(s)<3:
		return(s)
	elif len(s)>=3:
		return( s[:3]+s[:3]+s[:3] )
		
def slt(s):
	fe=3
	if len(s)<fe:
		fe=len(s)
	front=s[:fe]
	return(front+front+front)


def main():
	#s='Noa'
	#print( 	f0(s) )
	#s='Easy'
	#print( 	f0(s) )

	s='Nadadsfadsf'
	print( 	slt(s) )
	s='Easy'
	print( 	slt(s) )
	s='Ey'
	print( 	slt(s) )




if __name__=='__main__':
	main()



