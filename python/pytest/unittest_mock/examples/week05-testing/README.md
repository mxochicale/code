# mock, pytests

## Running pytests
```
cd $HOME/repositories/mxochicale/code/python/pytest/unittest_mock/examples/week05-testing
conda activate simpleVE


pytest test_times.py -s
pytest test_times.py -m test_negative_time_range 
pytest -k test_generic_case  -v

pytest test_times.py -v 
```