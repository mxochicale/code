#make_bricks.py
#We want to make a row of bricks that is goal inches long.
#We have a number of small bricks (1 inch each) and
#big bricks (5 inch each).
#Return True if it is possible to make the goal by 
#choosing from the giving bricks.
#This is a little harder than it looks and
#can be done without any loops


def mb(s,b,g):
	sb=s*1
	bb=b*5
	
	if (sb+bb)==g or bb==g or sb==g:
		return(True)
	return(False)

#Replicating Solution
#http://codingbat.com/doc/practice/makebricks-solution-code.htmlm
# video: https://www.youtube.com/watch?time_continue=323&v=pEw1sB13fjM


def sol(s,b,g):
	##fail #1 -- not enouhg brikcs
	if (g > b*5+s):
		return('not enogh bricks')

	##fail #2 -- not enough small bricks
	if (g%5)>s:
		return('not enogh small bricks')

	return(True)

def main():
	print( mb(3,1,8) )#True
	print( mb(3,1,9) )#False
	print( mb(3,2,10) )#True

	print( sol(3,1,9) )#False
	print( sol(1,4,12) )#False
	print( sol(3,1,8) )#True
	print( sol(3,2,10) )#True




if __name__=='__main__':
	main()
