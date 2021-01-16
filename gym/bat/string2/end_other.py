#end_other.py
#Given two strings, return True if either of the strings 
#appears at the very end of the other string,
#ignoring upper/lower cases differences 
#(in other words, the computation should not be 'case sensitive').
#Note: s.lower() returns lowercase version of a string.
#
 

def eo(a,b):
	a=a.lower()
	b=b.lower()
	
	La=len(a)
	Lb=len(b)
	ld=abs(La-Lb)

	#print( ld )
	#print(a[ ld:La ])
	#print(	 b[ ld:Lb ] )

	if La>Lb and a[ ld:La ] == b:
			return(True)
	if Lb>La and  b[ ld:Lb ] == a:
			return(True)
	
	if La==Lb and  a==b:
			return(True)
			
	return(False)

#Hint:
#In Python s1.endswith(s2) tests 
#if string s1 ends with string s2 -- makes this much easier!
def sol(a,b):
	a=a.lower()
	b=b.lower()
	
	if a.endswith(b) or b.endswith(a):
		return(True)
	return(False)

def main():
	print (  eo('hiABC','abc')  ) 
	print (  eo('aBC','adfadcabc')  ) 	
	print (  eo('aBc','adfadcAbC')  ) 

	print (  eo('hiABC','axbc')  ) 
	print (  eo('aBC','adfadcaixbc')  ) 

	print (  sol('hiABC','abc')  ) 
	print (  sol('aBC','adfadcabc')  ) 	
	print (  sol('aBc','adfadcAbC')  ) 

	print (  sol('hiABC','axbc')  ) 
	print (  sol('aBC','adfadcaixbc')  ) 


if __name__=='__main__':
	main()
