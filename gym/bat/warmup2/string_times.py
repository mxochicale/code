#string_times.py
#Given a tring and a non-negative int n, return a large string
#that is n copies of the origin string.


def st0(s,n):
	
	i=0
	sa=''
	while i<n:
		#print(i)
		i=i+1
		sa=sa+s	

	return(sa)


def slt(s,n):
	result=''
	for i in range(n):
		result=result+s
	return result


def main():
	n=5
	s='robot'
	print( st0(s,n) )
	
	print( slt(s,n) )



if __name__=='__main__':
	main()

