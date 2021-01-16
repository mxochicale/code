#squirrel_play.py
#The squirrels in Palo Alto spend most of the day 
#playing. In particular, they play if the temperature is
#between 60 and 90 (inclusive).
#Unless is summer, then the upper limit is 100
#instead of 90.
#Given int temperature and a boolean is_summer,
#return True if the squirrels play 
#and False otherwise.

def sp(t,s):
	if s==True:
		if t>=60 and t<=100:
			return(True)
	if t>=60 and t<=90:
		return(True)
	else:
		return(False)
	

def main():
	print( sp(50,True) )	
	print( sp(40,True) )	
	print( sp(60,True) )	
	print( sp(99,True) )	
	print( sp(60,False) )	
	print( sp(99,False) )	


if __name__=='__main__':
	main()

