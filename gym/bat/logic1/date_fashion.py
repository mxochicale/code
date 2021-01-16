#date_fashion.py
#You and your date are trying to get a table in a restaruant.
#The parameter of "you" is the styliness of your clothes,
#in the range of 0..10,
#and "date" is the styliness of your date's clothes.
#The result getting the table is endoced as an int value
#with 0=no and 1=yes.
#If either of is very stylish, 8 or more,
#then the result is 2 (yes).
#With the exeption that if either of you has style of 2
#or less, then the result is 0(no).
#Otherwise the result is 1 (maybe).
#


def df(y,d):
	if y>=8 or d>=8:
		return(2)
	if y<=2 or d<=2:
		return(0)
	else:
		return(1)


def main():
	print(df(5,10))	
	print(df(10,5))	

	print(df(5,2))	
	print(df(2,5))	

	print(df(5,5))	




if __name__=='__main__':
	main()
