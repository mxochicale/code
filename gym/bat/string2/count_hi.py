#count_hi.py
#Return the number of times that the string 'hi'
#appears anywhere in the give string.
#

def ch(s):
	h='hi'
	nh=0

	for i in range(0, len(s)-1 ):
		#print( s[i] )
		if s[i]+s[i+1] == 'hi':
			nh=nh+1
	
	return(nh)


def main():
	print( ch('hi, are you there, hi') )
	print( ch('hihi') )
	print( ch('hi hi hi') )

if __name__=='__main__':
	main()

