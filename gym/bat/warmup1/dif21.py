#Given an int n, return  the absolute difference between n and 21,
#except return double the absolute difference n over 21


def dif21(n):
	dif= abs(n-21)
	if n>21:
		return 2*dif
	else:
		return dif


def diff21(n):
	if n<=21:
		return 21-n
	else:
		return (n-21)*2



#n=19
#n=21
n=22

a=dif21(n)
print(a)


a=diff21(n)
print(a)



