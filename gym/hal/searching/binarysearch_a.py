def bs(v,key):
	lo=0
	hi=len(v)-1	
	#mid=  round( (hi+lo)/2 )
	#print('lo',lo, 'hi', hi, 'mid',mid  )	
	#print('v[lo]',v[lo], 'v[hi]', v[hi], 'v[mid]',v[mid]  )	
	#print(v[lo:(hi+1)])

	while lo<=hi:
		mid= round ( (hi+lo)/2 )  
		#print('lo',lo,'mid',mid, 'hi', hi )	
		print('lo',lo, 'hi', hi, 'mid',mid  )	
		print(v)
		
				
		if v[mid]<key:
			lo=mid+1
		elif v[mid]>key:
			hi=mid-1
		else:
			return mid	


	return -1 ## key no found

print('#####################')
v=list( range(0,4) )
### v=[0,1,2,3] ### v[0]=0, v[1]=1, v[2]=2, v[3]=3
print(  bs(v,4)  )


print('#####################')
v=list( range(0,5) )
### v=[0,1,2,3] ### v[0]=0, v[1]=1, v[2]=2, v[3]=3
print(  bs(v,4)  )






