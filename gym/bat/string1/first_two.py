#first_two.p
#Given am string, return the string made of its first two chars,
#so the String "Hello" yields 'He'.
#If the string is shorter than length 2, return whatever there is,
#so "X" yields 'X', and the empty string '' yields the empty string ''.



def ft0(x):
	#print(x)
	if len(x) >= 2:
		return(x[:2])
	return(x)		

def main():
	x=''
	print( ft0(x) ) 
	
	x='a'
	print( ft0(x) )   
	
	x='XXXX'
	print( ft0(x) )   



if __name__=='__main__':
        main()


