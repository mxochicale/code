#last2.py
#Given a string, return the count of the number of times that 
#a substring lenght 2 appers in the string and also as the last 2 chars
#of the string, so 'hixxxhi' yields 1
#(we won't count the end substring)



def lt0(s):
	ls=len(s)
	l2=s[(ls-2):ls]
	#print(l2)

	c=-1
	for i in range(ls-1):
		pair = s[i:(i+2)]
		if pair == l2:
			c=c+1
	return(c)
		
		
def slt(s):
	if len(s)<2:
		return 0
	#last two characters can be written as str[-2:]
	l2=s[len(s)-2:]
	
	count=0
	for i in range(len(s)-2):
		sub=s[i:i+2]
		if sub==l2:
			count=count + 1
	return count
	

def main():
	s='sdxxssd'
	print(	lt0(s) )
	print(	slt(s) )

	s='hixxxhi'
	print(	lt0(s) )
	print(	slt(s) )
	
	s='xaxxaxaxx'
	print(	lt0(s) )
	print(	slt(s) )

	s='axxxaaxx'
	print(	lt0(s) )
	print(	slt(s) )



if __name__=='__main__':
	main()


