#big_diff.py
#Given an array length 1 or more of ints,
#return the difference between the largest 
#and the smallest values in the array.
#Note: the built-in min(v1,v2) and max(v1,v2)
#functions return the smalles and the largest values.
#


def bd(x):
	
	vmaxac=max(x[0],x[1])  
	for i in range(1,len(x)-1):
		vmaxcu=max(x[i],x[i+1])
		if vmaxac>vmaxcu:
			vmax=vmaxac
		else:
			vmax=vmaxcu

	vminac=min(x[0],x[1])  
	for i in range(1,len(x)-1):
		vmincu=min(x[i],x[i+1])
		if vminac<vmincu:
			vmin=vminac
		else:
			vmin=vmincu


		
	#print(vmax)	
	#print(vmin)	
			


	return(vmax-vmin)


def main():
	print( bd([2,2,3])  )
	print( bd([10,3,5,7])  ) #7
	print( bd([7,2,10,9])  ) #8
	print( bd([2,10,7,2])  ) #8

if __name__=='__main__':
	main()


