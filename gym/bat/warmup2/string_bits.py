#string_bits.py
#Given a string, return a new string made of every
#other char starting with the first, so "Hello" yields 'Hlo'
#

from random import *

def sb0(x):
	lx=len(x)
	fc=x[0]
	nfc=x[1:lx]	
	#print(nfc)
	
	x=list(range(0,lx-1))
	shuffle(x)	

	ac=''
	for i in range(len(x)):
		#print(x[i])
		#print(  nfc[ x[i] ]  )
		ac=ac+nfc[ x[i] ]		
	#print(ac)
	
	return (fc+ac)

#Ther are many ways to do this, 
#as the one abore. 
#This one  uses the standard loop of i on every char,
#and inside the loop skips the odd index values.
def slt(x):
	result=''
	for i in range(len(x)):
		if i % 2 == 0:
			result = result + x[i]
	return result




def main():
	x='code'
	print( sb0(x) )
	
	print( slt(x) )



if __name__=='__main__':
	main()

