# Playing with: Draw the Mandelbrot Set in Python

## Setup your conda VE
See more details [here](../setting-virtual-environment)

##Scripts
1. Launch VE
```
conda activate playground-ve-cpu
```

2. Usage

Run a given script whose name starts with a number, for example:

```python
$ python 01_scatter_plot.py
```

## Running Code Style Checks

```
flake8
mypy .
black --check .
```

## Running Python Code Formatter
```
black .
```

## References
https://github.com/realpython/materials/tree/mandelbrot/mandelbrot-set-python
