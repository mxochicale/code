
## download


Deactivate any virtual environment: `conda deactivate`

```
cd
git clone --recursive https://github.com/datoviz/datoviz.git
cd datoviz
./manage.sh build
```

## test
```
./manage.sh demo
```

## compile with cython

```
./manage.sh cython
```

* issues
```
mxochicale@match-wx9:~/datoviz$ ./manage.sh cython
Traceback (most recent call last):
  File "utils/gencython.py", line 9, in <module>
    import pyparsing as pp
ModuleNotFoundError: No module named 'pyparsing'
```
* todo
* [ ] create conda virtual environment
* [ ] install these dependencies
```
NumPy
IPython
cython
pyparsing
colorcet
imageio
```
