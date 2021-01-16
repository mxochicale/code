# Given an int n return True if it is within 10 of 100 or 200
# Note: abs(num) computes the absolute value of a number

def near_hundred(n):
	di=abs(n-10)
	if n>=90 and n<=110:
		return True
	elif n>=190 and n<=210:
		return True
	else:
		return False


def near_hundred_sol(n):
	return(  (abs(100-n) <=10) or ( abs(200-n) <=10)  )


n=19

a=near_hundred(n)
print(a)



b=near_hundred_sol(n)
print(b)
