#front_times
#Given a string and non-negative int n,
#we will say that the front of the string is the first 3 chars 
#or whatever is there if the string is less than length 3. 
#Return n copies of the front.


def ft0(s,n):
	sl=len(s)
	#print(s[:2])	
	if sl<3:
		s3=s
	else:
		s3=s[:3]
	#print(s3)
	
	ac=''
	for i in range(n):
		ac=ac+s3
			
	return(ac)


def slt(s,n):
	front_len=3
	if front_len > len(s):
		front_len=len(s)
	front = s[:front_len]

	result=''
	for i in range(n):
		result = result + front
	return result
	


def main():
	n=2
	s='Coding'
	print(	ft0(s,n) )

	n=4
	s='Coding'
	print(	ft0(s,n) )


	n=4
	s='Coding'
	print(	slt(s,n) )



if __name__=='__main__':
	main()


