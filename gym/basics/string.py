
single_quote_character='a'
print(single_quote_character)

# you can assign both single quote sequences and 
# double quote sequence

double_quote_multiple_characters="aeiou"
single_quote_multiple_characters='aeiou'

print( type(double_quote_multiple_characters), type(single_quote_multiple_characters))

print( double_quote_multiple_characters is single_quote_multiple_characters )

triple_quote_example = """ this is a sentence written in triple quotes   """
print(type (triple_quote_example)  )

#### String common methods

# find the index of a "t" in a string "termometre"
print( 'termoetre'.index('t')  )
print( "abcd".index("c") )
print( 'i' in 'pythonic') 


combined_string=' '.join(['1', '2', '3'])
print(combined_string)
print( '1 2 3'.split()  )
print( '1:2:3'.split(':')  )

lang='python'
print( lang[0] )
for i in lang:
	print(i)

print('I love %s in %s' % ('programming', 'Python') )

# you can also the keyword format

print( ' I love {prog} in {p} '.format(prog='programming', p='Python')   )



