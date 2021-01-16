#cigar_party.py
#When squirrels get together to a party,
#they like to have cigars. A squirrel party is successful
#when numbers of cigars is between 40 and 60, inclusive.
#Unless it is the weekend, in which case there is no 
#upper bound on number of cigars. 
#Return True if the party with the given values is succesful,
#or false otherwhise.
#


def cp(x,d):

	if x>=40 and d==6 and d==7:
		return(True)
	if x>=40 and ( d>=0 or d<6):	
		return(True)
	return(False)

def main():
	c=41
	d=6
	print(cp(c,d))	
	c=40
	d=5
	print(cp(c,d))	

	c=39
	d=5
	print(cp(c,d))	


	c=70
	d=6
	print(cp(c,d))	




if __name__=='__main__':
	main()
