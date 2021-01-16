#double_char.py
#Given a string, return a string where for every char in the orignal,
#there are two chars.
#

def dc(s):
	ts=''
	for i in range(0,len(s)):
		#print( s[i] )
		ts=ts+s[i]+s[i]
	return( ts )

def main():
	print(  dc('hello') )
	print(  dc('Hi-There') )
if __name__=='__main__':
	main()

