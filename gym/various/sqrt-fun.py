
#https://interactivepython.org/runestone/static/CS152f17/MoreAboutIteration/Newton'sMethod.html

def newtonSqrt(n,howmany):
	approx=0.5 * n

	for i in range(howmany):
		betterapprox=0.5 * ( approx + n/approx )
		approx=betterapprox

	return(betterapprox)
	
def newtonSqrtWhile(n,howmany):
	approx=0.5*n
	better=0.5*(approx+n/approx)
	n=0
	while better != approx:
		n=n+1
		approx = better
		better=0.5*(approx+n/approx)
		print(n)

	return (aprox)
	

	

def main():
	n=10
	print(	newtonSqrt(n,2)   ) 
	print(  newtonSqrtWhile(n,2)  )

if __name__=='__main__':
	main()

