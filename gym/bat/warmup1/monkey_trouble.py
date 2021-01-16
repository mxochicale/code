##monkey_trouble.py
#We have two monkeys, a and b, and the parameters 
#a_smile and b_smile indicate if each is smilling.
#We are in trouble if they are both smilling or
#if neither of them is smilling. 
#Return True if we are in trouble
#

def mt0(ma,mb):
	if ( ma == mb  ):
		return ('Monkeys are smiling: We are in trouble')
	else:
		return('we are NOT in trouble')	
	
def mt1(a,b):
	if a and b:
		return True
	if not a and not b:
		return True
	return False

def mt2(a,b):
	return ( (a and b) or (not a and not b)  )



def main():
	print('#### My solution')
	print( mt0(False,False) )
	print( mt0(False, True) )
	print( mt0(True, False) )
	print( mt0(True, True) )

	print('#### First solution')
	print( mt1(False,False) )
	print( mt1(False, True) )
	print( mt1(True, False) )
	print( mt1(True, True) )

	print('#### Second solution')
	print( mt2(False,False) )
	print( mt2(False, True) )
	print( mt2(True, False) )
	print( mt2(True, True) )




if __name__ == '__main__':
	main()
