def sign(x):
	if x>0:
		return 'positive'
	elif x<0:
		return 'negative'
	else:
		return 'zero'


for idx in [-2, -1, 0, 1, 2]:
	print(sign(idx))
