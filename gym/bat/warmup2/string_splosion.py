#string_splosion.py
#Five a non-empty strink like 'Code'
#return a string like 'CCoCodCode'
#

def ss(s):
	n=len(s)
	
	ac=''
	for i in range(1,n+1):	
		ac= ac + s[0:i] 
	return(ac)	
	
		
def slt(s):
	result=''
	for i in range(len(s)):
		result=result+s[:i+1]
	return(result)

def main():
	s='Code'
	print(	ss(s)  )
	print(	slt(s)  )




if __name__=='__main__':
	main()

