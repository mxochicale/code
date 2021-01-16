#parrot_trouble.py

#We hav ea loud talking parrot. 
#The 'hour' parameter is the curren hour time in the
#range 0..23. We are in trouble if the parrot
#is taling and the hour is before 7 or after 20.
#Return True if we are in trouble
#

def pt0(p,h):
	if (  ( h>0 and h<7) or (h>20 and h<24) ) and (p==True ):
		return(True)
	return(False)


def sol(talking, hour):
	return ( talking and ( hour<7 or hour>20 ) )
	

def main():
	
	for i in range(0,24):
		print (i, pt0(True,i) )
		print (i, sol(True,i) )

if __name__ == '__main__':
	main()

