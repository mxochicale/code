#love6.py
#The number 6 is a truly great number.
#Given two int values, a and b, return True 
#if either of them is 6 or if their sum 
#or difference is 6.
#Note the function abs(num) 
#compute the absolute value of num.
#

def s(a,b):
	if a==6 or b==6:
		return(True)
	elif (a+b)==6:
		return(True)
	elif abs(a-b)==6:
		return(True)
	else:
		return(False)


def main():
	print(s(3,3))
	print(s(6,3))
	print(s(5,6))
	print(s(2,4))
	print(s(8,2))

	print(s(1,2))



if __name__=='__main__':
	main()

