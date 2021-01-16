#has23.py
#Given an array int length 2, return true 
#if it contains a 2 or a 3.
#

def h(x):
	if x[0]==2 or x[0]==3:
		return(True)
	if x[1]==2 or x[1]==3:
		return(True)
	return(False)
	
def main():
	x=[1,2]
	print(h(x))
	x=[2,1]
	print(h(x))
	x=[1,3]
	print(h(x))
	x=[3,1]
	print(h(x))
	x=[1,1]
	print(h(x))





if __name__=='__main__':
	main()
