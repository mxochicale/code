
def sum(L,s):

	stmp=[-1,-1]
	for i in range (0, len(L)):
		for k in range (0, len(L)):
			#print(i,k)
			#print(L[i],L[k])
			sumi=L[i]+L[k]
			if s==sumi:
				sik= [i, k]
				stmp= sik


	return(stmp)
					
			

def main():
	L=[11,22,33,44,55]
	s=100
	print( sum(L,s))

if __name__=='__main__':
	main()
