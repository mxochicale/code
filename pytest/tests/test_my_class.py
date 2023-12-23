from unittest.mock import patch
# https://kimsereylam.com/python/2021/03/19/how-to-use-patch-in-python-unittest.html

class MyClass:
    my_class_attribute = 1

    def __init__(self):
        self.instance_attribute_value = 2

    def method_do_something(self):
        return f"hello {self.instance_attribute_value}"


def test_instance_attribute_value():
    o = MyClass()
    with patch.object(o, "instance_attribute_value", return_value=33):
        print(f"PRINT o.instance_attribute_value: {o.instance_attribute_value()}")
        assert o.instance_attribute_value() is 33

def test_path_my_class_attribute():
    o = MyClass()
    with patch.object(o, "my_class_attribute", return_value=3):
        print(f"PRINT o.my_class_attribute: {o.my_class_attribute()}")
        assert o.my_class_attribute() is 3

def test_patch_method_do_sth():
    o = MyClass()
    with patch.object(o, "method_do_something", return_value="hello"):
        print(f"PRINT: o.method_do_something(): {o.method_do_something()}")
        assert o.method_do_something() is "hello"



