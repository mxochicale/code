## Loops and conditionals

fruits = ['apples', 'oranges', 'mangoes']
for fruit in fruits:
	print(fruit)

print('####')

for fruit in fruits:
	#print(fruit)
	string_size=0
	for alphabet in fruit:
		string_size+=1
		#print(string_size)
	print('name of fruit: %s has lenght %s' % (fruit, string_size) )


fruits = ['apples', 'oranges', 'mangoes']
for idx, fruit in enumerate(fruits):
	print('idx %s' % idx)
	print('fruit %s' % fruit)
	print('##################')
	


#### while statement

fruits = ['apples', 'oranges', 'mangoes']
length = len(fruits)
print('len fruits:', length)
i=0
while i<length:
	print(i)
	print(fruits[i])
	i+=1

### nested loops
for i in range(1,3):
	for j in range(1,3):
		print('%d x %d = %d' % (i,j,i*j) )


### if statement
num=42
if num==42:
	print('number is 42')

### adding a else block
n=43
if n==42:
	print('number is 42')
else:
	print('number is not 42')


### adding elif block

n=44
if n==42:
	print('number is 42')
elif n==44:
	print('number is 44')
else:
	print('number is neither 42 nor 44')


### nested if
n=20.1
if n>20:
	if n<50:
		print('%f is between 20 and 50' % n )






