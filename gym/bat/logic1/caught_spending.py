#caught_spending.py
#You are driving a little too fast, and a police 
#officer stops you. Write code to compute the result,
#encoded as an int value: 
#0=no ticket,
#1=small ticket,
#2=big ticket.
#If speed is 60 or less, the result is 0.
#If speed is between 61 and 80 inclusive, the result is 1.
#If speed is 81 or more, the result is 2.
#Unless it is your birthday -- on that day
#your speed can be 5 higher in all cases.
#

def cs(v,B):
	if B==True:	
		e=5
	else:
		e=0
	if v>=(0+e) and v<=(60+e):
		#print( 0+e)
		return(0)		
	elif v>=(61+e) and v<=(80+e):
		return(1)		
	elif v>=(81+e):
		return(2)




def main():
	print(cs(60, False))
	print(cs(65, False))
	print(cs(65, True))

	print(cs(61, False))
	print(cs(61, True))
	
	print(cs(80, False))
	print(cs(85, False))
	print(cs(85, True))

	


if __name__=='__main__':
	main()



