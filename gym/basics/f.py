# adding two numbers

def add2numbers(n1,n2):
	'returns the sum of n1 and n2'
	r=n1+n2
	return r

print( add2numbers(2.4,2) )



sum = add2numbers(2.4,412321) 
print(sum)

print('###')

def maw(v):
	vl=len(v)
	i=0
	m=1
	while i < vl:
		#print( i )
		print( v[i] )
		m*=v[i]
		i+=1

	
	return(m)

v=[1,2,3,4]
print(	maw(v) )	

print('###')


def maf(vec):
	m=1
	for val in vec:
		m*=val
	return(m)


f=maf( [1,2,3,.5] )
print(f)


def string_mult(str_arg, number):
	'string and multiples with a number'
	return str_arg*(number+1)


sm=string_mult('X',5)
print(sm)


#sm=string_mult(5,'X')
#print(sm)



