#string_match.py
#Given 2 strings, a and b, return the 
#number of the positions where they contain the same lenght 2 substracting.
#So "xxcaazz" and "xxbaaz" yields 3, since "xx", "aa", and "az" subtrings
#appear in the same place in both strings.
#



def sm0(a,b):
	la=len(a)
	lb=len(b)

	if la<lb:
		lfor=la-1
		amax=a
		amin=b
	elif la==lb:
		lfor=la-1
		amax=a
		amin=b
	else:
		lfor=lb-1
		amax=b
		amin=a

	count=0
	for i in range(0,lfor):
		#print(amax[i:i+2])
		#print(amin[i:i+2])
		if amax[i:i+2] == amin[i:i+2]:
			count=count+1


	return(count)


def slt(a,b):
	shorter=min( len(a), len(b))
	count=0

	#Loop for every substring starting spot
	#Use lenght-1 here, so can use char str[i+1] in the loop
	for i in range(shorter-1):
		a_sub=a[i:i+2]
		b_sub=b[i:i+2]
		if a_sub==b_sub:
			count=count+1
	return(count)


def main():
	a='xxcaazz'
	b='xxbaaz'
	print( sm0(a,b) )
	print( slt(a,b) )
	
	a='xxbaaz'
	b='xxcaazz'
	print( sm0(a,b) )
	print( slt(a,b) )

	a='abc'
	b='abc'
	print( sm0(a,b) )
	print( slt(a,b) )
	a='abc'
	b='axc'
	print( sm0(a,b) )
	print( slt(a,b) )





if __name__=='__main__':
	main()


