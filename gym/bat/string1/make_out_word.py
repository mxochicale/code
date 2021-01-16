#make_out_word.py
#Given an "out" string lenght 4m such as "<<>>",
#and a word, return a new string where the word
#is in the middle of the out string, e.g. "<<word>>"

def moo0(o,w):
	return( o[:2]+w+o[-2:])


def main():
	o='<<>>'
	w='gan'
	print ( moo0(o,w) )

	o='[[]]'
	w='GAN'
	print ( moo0(o,w) )



if __name__=='__main__':
	main()

