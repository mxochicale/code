#in1to10.py
#Given a number n, return True if n is in the range 1..10,inclusive.
#Unless outside_mode is True, in which case return 
#True if the number is less or equal to 1 or greater or equal to 10.
#


def i(n,outside_mode):
	if (outside_mode==False or outside_mode==True) and (n>=1 and n<10):
		return(True)
	elif outside_mode==True and n>=10:
		return(True)
	elif outside_mode==True and n<=1:
		return(True)
	else:
		return(False)


def main():
	print( i(12,True)) #True
	print( i(12,False)) #False
	print( i(-12,True)) #True
	print( i(-12,False)) #False


	print( i(8,True)) # True
	print( i(8,False)) # True

if __name__=='__main__':
	main()

