#near_ten.py
#Given an 'non-negative' number num,
#return True if the number is within 2 of  a multiple 10.
#NOTE: (a%b) is the remainder of dividing a by b,
#so (7%5) is 2
#

def n(n):
	r=n%10
	#print(r)
	if r==9 or r==8:
		return(True) 
	elif r>=0 and r<=2:
		return(True) 
	else:
		return(False)



def main():
	print( n(7)  ) #3 FALSE
	print( n(8)  ) #2 TRUE
	print( n(9)  ) #1 TRUE
	print( n(10)  ) #0 TRUE
	print( n(11)  )
	print( n(12)  )
	print( n(13)  ) # FALSE
	
	print( n(17)  ) # FALSE
	print( n(19)  ) # TRUE


if __name__=='__main__':
	main()

