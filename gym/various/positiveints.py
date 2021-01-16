



def testOne():
	N=10
	n=N+1
	for a in range(1,n):
		for b in range(1,n):
			for c in range(1,n):
				for d in range(1,n):
					if a*a*a + b*b*b == c*c*c + d*d*d:
						print(a,b,c,d)


def testTwo():
	#n=2
	#a=pow(9,1/2)
	#print(a)
	N=2
	n=N+1
	map=[]
	for c in range(1,n):
		for d in range(1,n):
			result=pow(c,3)+pow(d,3)

			map.append( [('c',c),('d',d),('result',result)] )
	
			# append(c,d) to list at value map[results]

	print(map)
	print(dict(map))
	#print( map.get("result")  )

#
#	list=[]
#	for a in range(1,n):
#		for b in range(1,n):
#			result=pow(a,3)+pow(b,3)
#			list=map.get(result)
#
#	print(list)	
#
	
def main():
	#testOne()
	testTwo()

if __name__=='__main__':
	main()
