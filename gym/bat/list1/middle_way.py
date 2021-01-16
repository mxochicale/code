#middle_way.py
#Given 2 int arrays, a and b, each length 3,
#return a new array length 2 containing the middle element

def mw(a,b):
	return([a[1],b[1]])

def main():
	a=[1,1,3]
	b=[1,2,3]
	print(mw(a,b))

if __name__=='__main__':
	main()
