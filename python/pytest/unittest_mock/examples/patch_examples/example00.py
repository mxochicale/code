import pytest
from mock import call

# References
# https://stackoverflow.com/questions/53434986/using-mocker-to-patch-with-pytest

def sum(a, b):
	"""
	Addition function
	"""	
	return a + b

def test_sum0():
	a=2
	b=3
	expected=5
	assert sum(a,b)==expected

def test_sum1(mocker):
    mocker.patch(__name__ + ".sum", return_value=9)
    assert sum(2, 3) == 9


def test_sum2(mocker):
    def crazy_sum(a, b):
        return b + b

    mocker.patch(__name__ + ".sum", side_effect=crazy_sum)
    assert sum(2, 3) == 6


