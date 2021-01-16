#sorta_sum.py
#Given 2 ints, return their sum.
#However, the sum 10..19 inclusive, are forbidden,
#so in that case return 20.
#

def ss(a,b):
	s=a+b
	if s>=10 and s<=19:
		return(20)
	else:
		return(s)



def main():
	print(ss(2,5))
	print(ss(5,5))
	print(ss(10,9))
	print(ss(10,11))

if __name__=='__main__':
	main()
