
############################
print('####################')
print('NUMBERS')

x=3
print( type(x) )
print(x)
print(x-1)
print(x+1)
print(x*2)
print(x**3) #Exponentiation 
print('---------')
x += 1
print(x)
print('---------')
x *=2
print(x)


print('---------')
y=2.5
print(type(y))
print(y,y+1, y**2,   )


############################
print('####################')
print('BOOLEANS')

t = True 
f = False

print(type(t))
print ( t or f )
print ( t and f )
print (  not t )


############################
print('####################')
print('STRINGS')
hello = 'hello'
world = 'world'
print(hello)
print(len(hello))

hw = hello + ' ' + world
print(hw)

print ( '%s %s %d' % (hello, world, 66)   )


s='xochicale'

print(s.capitalize())
print(s.upper())
print(s.replace('l', '(LL)' ))



############################
#print('####################')
#print('CONTAINERS')

print('####################')
print('lists')

xs = [3,1,2]
print(xs,xs[0], xs[-2])
xs[2]= 'foo'
print(xs)
xs.append('ban')
print(xs)
xs.append([1,2,3])
print(xs)
x=xs.pop()# remove the last element of the list
print(x)


print('####################')
print('slicing')

nums = list(range(10))
print(nums)
print(nums[2:5])
print(nums[:5])
print(nums[2:])
print(nums[:])

print('####################')
print('## list:loops')

animals = ['dog','cat','monkey']
for animal in animals:
	print(animal)

for idx, animal in enumerate(animals):
	print('#%d: %s' % (idx+1, animal)   )

print('####################')
print('## list:loops:comprehensions')
nums = list(range(5))
squares = []
for x in nums:
	squares.append(x ** 2)

print(squares)

nums = list(range(5))
squares = [ x**2 for x in nums  ]
print(squares)

nums = list(range(5))
even_squares = [ x**2 for x in nums  if x % 2 == 0 ]
print(even_squares)


print('####################')
print('## dictionaries')

d = { 'cat':'cute', 'dog':'furry' }
print(d['cat'])
print('cat' in d ) # check if a dictionary has a given key
d['fish']='wet'

print(d.get('monkey','N/A'))
print(d.get('fish','N/A'))
del d['fish']
print(d.get('fish','N/A'))


print('####################')
print('## loops:dictionaries')
d = {'person':2, 'cat':4, 'spider':8}
for animal in d:
	legs=d[animal]
	print( 'A %s has %d legs' % ( animal,legs ) )


print('####################')
print('## dictionaries:comprehensions')
nums=[0,1,2,3,4]
even_num2square = {x: x**2 for x in nums if x % 2 == 0}
print(even_num2square)


print('####################')
print('## sets')

animals = {'cat','dog'}
print('cat'  in animals)
print('fish'  in animals)
animals.add('fish')
print('fish'  in animals)

print( len(animals))
animals.add('cat') # adding an element that is already in the set does nothing
print( len(animals))
animals.remove('cat')
print( animals )


animals = {'cat','dog','fish','monkey'}
for idx, animal in enumerate(animals):
	print( '#%d: %s' % (idx+1, animal )  )

print('####################')
print('## turples')

d={(x,x+1): x for x in range(10) }
print(d)
t=(5,6)
print(type(t))
print(d[t])
print(d[(3,4)])











