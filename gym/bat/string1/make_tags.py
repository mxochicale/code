#make_tags.py
#The web is built with HTML strings like "<i>Yay</i>" which draws Yay in italics.
#In this example, the "i" tag makes <i> and </i> which sorrounds the word "Yay"/
#Given a tag and word strings, create the HTML string with tags around the word, e.g.
#"<i>Yay</i>"


def mt0(tag,x):
	return ( '<'+tag+'>'+x+'</'+tag+'>' )


def main():
	tag='cite'
	x='Yay'
	print ( mt0(tag,x) )

if __name__=='__main__':
	main()

