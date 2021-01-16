#xyz_there.py
#Return True if the given string contains an 
#appearance of 'xyz' where the xyz is not 
#directly proceeded by a period(.).
#So 'xxyz' counts but 'x.xyz' does not.
#


def there(x):
	for i in range(0, len(x)-3):
		#print (  x[i]+x[i+1]+x[i+2]+x[i+3]  ) 
	
		if x[i]+x[i+1]+x[i+2]=='xyz' or (x[i]!='.' and x[i+1]+x[i+2]+x[i+3]=='xyz' ):
			return(True)
		if x[i]=='.' and x[i+1]+x[i+2]+x[i+3]=='xyz':
			return(False)
	return(False)



def main():
	print( there('ixxyz') )	
	print( there('i.xyz') )	


	print ( there('abcxyz') )#→ True
	print ( there('abc.xyz')) #→ False
	print ( there('xyz.abc')) #→ True

if __name__=='__main__':
	main()
 
