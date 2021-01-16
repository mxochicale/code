def ts(v,l,r,x):	
	odt= int((r-l)/3 )
	m1=  l+ odt 
	m2=  r- odt 
	print('idx:',m1,m2)
	#print(v[m1], v[m2])

	if (v[m1]==x):
		return m1
	if (v[m2]==x):
		return m2
	
	if (x < v[m1]):
		return ts(v,l,m1-1,x)
	elif (x > v[m2]):	
		return ts(v,m2+1,r,x)
	else:
		return ts(v,m1+1,m2-1,x)

	return -1


	

#        m1          m2
#  0  1  2  3  4  5  6   7   8
v=[2, 3, 5, 6, 8, 9, 12, 13, 14]
l=0 
r=8
x=8

print( ts(v,l,r,x) )
