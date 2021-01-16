#centered_average.py
#Return the 'centered' average of an array of ints,
#which we will say is the mean average of the values,
#except ignoring the largest and the smallest values in the array.
#If there are multiple copies of the smallest value,
#ignore just one copy, and likewise for the largest value.
#Use int division to produce the final average.
#You may assume that the array is length 3 or more.
#

def ca(x):
	l= largest(x) 

	for i in range(0,len(x)):
		if x[i]==l:
			di=i
			#print(di)

	nx=list(range(0, len(x)-1  ))
	xi=-1
	for i in range(0,len(nx)):
		xi=xi+1
		if i==di:
			xi=xi+1
		nx[i]=x[xi]

	#vector without the one of the maximum values
	#print(nx)


	s= smallest(nx) 
	for i in range(0,len(nx)):
		if nx[i]==s:
			di=i


	nnx=list(range(0, len(nx)-1  ))
	xi=-1
	for i in range(0,len(nnx)):
		xi=xi+1
		if i==di:
			xi=xi+1
		nnx[i]=nx[xi]

	#vector wihtout either one of the max and one of the min vals
	#print(nnx)


	s=0
	for i in range(0,len(nnx)):
		s=s+nnx[i]
	
	#av= s/len(nnx)##float division
	av= s//len(nnx)##int division

	return(av)




def largest(x):
	l=x[0]
	for i in range(0,len(x)):
		if x[i]>l:
			l=x[i]	
	return(l)

def smallest(x):
	s=x[0]
	for i in range(0,len(x)):
		if x[i]<s:
			s=x[i]	
	return(s)


def main():
	print(  ca( [1,2,3,4,100]  ))
	print(  ca( [1,1,5,5,10,8,7]  ))
	print(  ca( [-10,-4,-2,-4,-2,0]  ))


#	print(  ca( [1,2,100,2,3]  ))
#	print(  ca( [1,2,1,100,3]  ))
#	print(  ca( [100,2,1,4,3]  ))
#	print(  ca( [200,-1,2,3,4,100]  ))
#	print(  ca( [200,-1,100,1,4,3]  ))



if __name__=='__main__':
	main()

