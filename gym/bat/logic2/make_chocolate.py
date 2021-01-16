#make_chocolate.py
#We want make a package of "goal" kilos of chocolate.
#We have small bars (1 kile each) and big bars (5 kilos each).
#Return the number of small bars to use, assuming we always
#use big bars before small bars.
#Return -1 if it can't be done.
#

def mk(s,b,g):
	b=b*5
	s=s*1
	sg=g-b
	
	if sg<=s:
		return(sg)
	return(-1)	
	

def main():
	print( mk(4,1,9) )#4
	print( mk(4,1,10) )#-1
	print( mk(4,1,7) )#2


if __name__=='__main__':
	main()
