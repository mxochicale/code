#Giving a non-empty string and an int n,
#return a new string where the chart at index n
#has been removed.
#The value of n will be a vallid index of a char
#in the original string (i.e. will be in the range
#0..len(str)-1 inclusive).

def mc0(s,n):
	#print(s)
	#print(s[n])	
	#a='x'*len(s)
	n=n+1
	print(	s[:n-1]  + s[n:] ) 
	#for i in range(0,len(s)):
		#print( s[i] )
		#print( a[i] )
	#	a[i]=s[i:]
		#print(a)

	print 
#	return(	s.replace(s[n], '') )
	
def mc1(s,n):
	r=s.replace(s[n], '') 
	print(r)
	return(	r )

def mc2(s,n):
	front=s[:n]
	back=s[n+1:]
	r= front+back
	print(r)
	return(r)
	

def main():
	sr='machine'
	n=2
	mc0(sr,n)
	mc1(sr,n)
	mc2(sr,n)


if __name__ == '__main__':
	main()

