from my_package.mod_a.file_a import *
from my_package.mod_b.file_b import *
from my_package.mod_c.file_c import function_c

def main():
	print("Hello new package")
	function_c()
	function_a()
	function_b()

if __name__=='__main__':
	main()
