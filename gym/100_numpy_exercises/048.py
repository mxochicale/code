# 48 	Print the minium and maximum
#	representable value for each
# 	numpy scalar type

import numpy as np

def main():
	#for dtype in [np.int8, np.int32, np.int64]:
	#	print(np.finfo(dtype).min)

	for dtype in [np.float32, np.float64]:
		print(np.finfo(dtype).min)
		print(np.finfo(dtype).max)
		print(np.finfo(dtype).eps)


if __name__=='__main__':
	main()
