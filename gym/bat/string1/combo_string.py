#combo_string.py
#Given 2 strings, a and b, return a string of the form 
#short+long+short,
#with the shorter string on outside and the longer 
#string in the inside. The string will not be the same
#length, but they may be empty (lenght 0)


def cs(a,b):
	la=len(a)
	lb=len(b)
	if la>lb:
		return(a+b+a)
	elif la<lb:
		return(b+a+b)
	elif la==lb:
		return('none')

def main():
	a=''
	b='coding'
	print( cs(a,b) )

	a='xx'
	b='coding'
	print( cs(a,b) )

	a='xadsfadfsx'
	b='coding'
	print( cs(a,b) )

	a='xadsfa'
	b='coding'
	print( cs(a,b) )




if __name__=='__main__':
	main()
