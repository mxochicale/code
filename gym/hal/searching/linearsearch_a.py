

#############################
def ls(v):
	for i, vi in enumerate(v):
		#print( i )
		#print(v[i])
		if (v[i]==7):
			return i 	



v=[1,2,3,3,3,5,7,3]
print( ls(v) )

v=[1,7,3]
print( ls(v) )





#############################
print('### function lo(A,M)')

def lo(A,M):
	N=len(A)
	i=N-1
	while i>=0:
		#print('i:',i)
		#print('i:',A[i])
		if A[i]==M:
			return i	
		i-=1	

	val=-1
	
	return val



A=list(range(0,10))
M=6
fc=lo(A,M)

print(fc)



