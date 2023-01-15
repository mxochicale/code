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

# ## Import python packages

import matplotlib.pyplot as plt
import numpy as np

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
# > https://pynative.com/python-nested-loops/

# +
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
# ## Plot 3D/voxels_simple
# > https://matplotlib.org/stable/plot_types/3D/voxels_simple.html#sphx-glr-plot-types-3d-voxels-simple-py
#

# +
# plt.style.use('_mpl-gallery')
# plt.style.use('_mpl-gallery-nogrid')

# Prepare some coordinates
x, y, z = np.indices((10, 10, 10))

# Draw cuboids in the top left and bottom right corners
cube1 = (x < 2) & (y < 2) & (z < 5)
cube2 = (x >= 8) & (y >= 2) & (z >= 8)

# Combine the objects into a single boolean array
voxelarray = cube1 | cube2
print(f' voxelarray.shape: {voxelarray.shape}')

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.voxels(voxelarray, edgecolor='k')

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
# -



