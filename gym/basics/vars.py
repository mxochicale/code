###############
## ASSIGNMENT

speed_of_light = 299792458
print(speed_of_light)

pi = 3.14
print(pi)

fav_lang='python'
print(fav_lang)


#############
## valid and invalid ways of assiging variables

# multiple word='multiple world'# error
# use underscore in the name
multiple_word = 'multiple word'
print(multiple_word)

# do not start with a number but after the name
var1=1
print(var1)

# youc an only include a-z, A-Z, and 0-9 with no special characters

############
## more on assigning

fav_writers = ['Mark Twain', 'Octavio Paz']
print(fav_writers)

###########
## assign dicts
birthdays = {'mom':'9jan', 'daughter':'23dec'}
print(birthdays)


#### assigning functions
import functools
memoize = functools.lru_cache
print(memoize)


### class assigment
class MyClass:
	pass

give_me_more = MyClass()
print(give_me_more)

### working with variables
var = 2
print(var + 3)
#number = input()
number = 3
type(number)
number=int(number)



print( range(5) )
r=range(4)
print(r)


id1, id2, id3 = range(3)
print(id1)
print(id2)
print(id3)

