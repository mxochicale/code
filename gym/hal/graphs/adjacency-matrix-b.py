

def initialise():
	n=10
	m=10		
	matrix = [[0 for i in range(n)] for j in range(m)]
	return(matrix)


def main():
	nodes=4
	edges=5
	A=initialise()
	print(A)


if __name__=='__main__':
	main()


