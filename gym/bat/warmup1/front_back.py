##front_back.py
#given a string, return a new string 
#where the first and last character have been exchanged

def fb0(s):
	n=len(s)
	#print(n)
	#print( s[n-1],  s[1:(n-1)], s[0] )
	if n>1:
		return( s[n-1] + s[1:(n-1)] + s[0] )
	return (s)

def sol(s):
	if len(s)<=1:
		return(s)
	mid = s[1:-1]
	return( s[len(s)-1]+mid+s[0])



def main():
	print( fb0('hello') )
	print( fb0('code') )
	print( fb0('ab') )
	print( fb0('a') )
	

	print( sol('hello') )
	print( sol('code') )
	print( sol('ab') )
	print( sol('a') )




if __name__=='__main__':
	main()




