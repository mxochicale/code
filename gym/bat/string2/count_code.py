#count_code.py
#Return the number of times that the 
#string 'code' appears anywhere in the
#given string, except we will 
#accept any letter for 'd' so 
#'cope' and 'cooe' count.
#


def cc(s):
	ncoe=0
	for i in range(0, len(s)-3):
		#print( s[i]+s[i+1]+s[i+3] )
		if s[i]+s[i+1]+s[i+3]=='coe':
			ncoe=ncoe+1
	return(ncoe)		



def main():
	print( cc('asdfadfcoxeadsfa') )
	print( cc('codeasdfadfcoxeadsfa') )
	print( cc('codeasdfadfcodead coxesfa') )

if __name__=='__main__':
	main()

