###sum_double
##Given two int values, return their sum.
##Unless the two values are the same, 
##then return double their sum

def sd0(a,b):
	#print(a,b)
	if a!=b:
		return(a+b)
	return(2*(a+b))

def s(a,b):
	s=a+b
	if a==b:
		s=2*s
	return(s)

def main():
	print(sd0(2,3))
	print(sd0(2,2))

	print(s(2,3))
	print(s(2,2))



if __name__=='__main__':
	main()

