# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Simple Equation
# Let us now implement the following equation
# $$y=x^2$$
# where $x=36$

x=36
y=x*x
print(y)

# +
#empty cell
# -

# ## Nested loop section

# +
# https://pynative.com/python-nested-loops/
numbers = [[11, 22, 33], 
           [4, 5, 6], 
           [7, 8, 9]]

cnt = 0
for i in numbers:
    print(f'  numbers[i]: {i}')
    for j in i:
        print(f'     index: {j}; count {cnt}')
        cnt = cnt + 1
# -




