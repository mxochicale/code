
def checkingN(N):
	N=int(N)
	if N>=1 and N<=10e5 :
		return(N)
	else: 
		print( 'N is restricted ')


def checkingM(M):
	M=int(M)
	if M>=1 and M<=10e9 :
		return(M)
	else: 
		print( 'M is restricted ')

def checkingA(A):
	for i in range(0,len(A)):
		Ai=int(	A[i] )
		if Ai>=1 and Ai<=10e9:
			return(Ai)
		else:
			return('Ai is restricted')

def fun(N,M):


	array=list(range(0,N))
	#print(array)

	checkingA(array)
	
#	for i in range(0,N):
#		ii= array[i] 
#		if ii==M:
#			return(M)
#		elif ii!=M:
#			return(-1)
#

	i=N-1
	while i>0:
		#print(array[i])
		if array[i]==M:
			return (M)
		i-=1


def main():
	a=fun(5,2)
	print(a)


	#print(	checkingN(10e6) )
	#checking(1000000,3)



if __name__=='__main__':
	main()

