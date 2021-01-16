#Declare global variable name for use in all functions
name = str(input('Enter your name: '))


#Define a function to check if names contains a vowel
def has_vowel():
	if set('aeiou').intersection(name.lower()):
		print('Your name contains a vowel.')
	else:
		print('Your name does not contain a vowel.')


# Iterative over letters in name string
def print_letters():
	for letter in name:
		print(letter)



# Define main method that calls other fuctions
def main():
	has_vowel()
	print_letters()


# Execyte the main() function
if __name__ == '__main__':
	#main()
	has_vowel()
	print_letters()

#In Python, '__main__' is the name of the scope where 
#top-level code will execute. When a program is 
#run from standard input, a script, or from an 
#interactive prompt, its __name__ is set equal to '__main__'.


