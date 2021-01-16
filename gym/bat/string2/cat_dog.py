#cat_dog.py
#Return True if the string 'cat' and 'dog'
#appear appear the same number of times 
#in the given string.
#


def cd(s):
	
	nc=0
	nd=0
	for i in range(0,len(s)-2):
		if s[i]+s[i+1]+s[i+2]=='cat':
			nc=nc+1
		if s[i]+s[i+1]+s[i+2]=='dog':
			nd=nd+1

	if nc==nd:
		return(True)
	
	return(False)		


def main():
	print (  cd('catdog'  )   )
	print (  cd('catcatdg'  )   )
	print( cd(' 1cat1cadogdo ')  )
if __name__=='__main__':
	main()

