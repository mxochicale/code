
# https://kimsereylam.com/python/2021/03/19/how-to-use-patch-in-python-unittest.html

class MyClass:
    my_attribute = 1

    def __init__(self):
        self.value = 2

    def do_something(self):
        return f"hello {self.value}"

def get_value():
	o = MyClass()
	return o.value

print( get_value() )

def do_sth():
	o = MyClass()
	return o.do_something()

print( do_sth() )

## TEST
from unittest.mock import patch

def test_myclass():
	with patch("my_class.MyClass") as mock:
    		mock.return_value.value = "hello"
    		print(get_value())



