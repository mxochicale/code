def func(x):
	um = -1*x*x + 2*x + 3
	return um


#print(  func(1.3) )

def ts(l,r):
	for i in range(0,100):
		#print(i)
		l1=(l*2+r)/3
		l2=(l+2*r)/3
		print( func(l1), func(l2) )
		if (func(l1) > func(l2) ):
			r=l2
		else:
			l=l1


print(ts(0,1))
