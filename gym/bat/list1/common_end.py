#common_end.py
#Given arrays of ints, a and b, return true if they 
#have the first element or they have the same last element.
#Both arrays will be lenght 1 or more.
#


def ce(a,b):
	
	if len(a)>1 and len(b)>1:
		if a[0]==b[0] or a[len(a)-1]==b[len(b)-1]:
			return(True)
	return(False)


def main():
	a=[1,2,3,4]
	b=[1,2,3,2]
	print (  ce(a,b) )
	a=[2,2,3,4]
	b=[1,2,3,4]
	print (  ce(a,b) )
	a=[2,2,3,4]
	b=[1,2,3,3]
	print (  ce(a,b) )

	a=[2]
	b=[1]
	print (  ce(a,b) )

	a=[1,3,4]
	b=[3,2]
	print (  ce(a,b) )





if __name__=='__main__':
	main()

