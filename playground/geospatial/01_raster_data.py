#https://rasterio.readthedocs.io/en/stable/topics/plotting.html
#https://github.com/rasterio/rasterio?tab=readme-ov-file#example

import numpy as np
import rasterio
import matplotlib.pyplot as plt 
from rasterio.plot import show
from rasterio.plot import show_hist

#Rasterio gives access to properties of a geospatial raster file.
with rasterio.open('data/RGB.byte.tif') as src:
    print(src.width, src.height)
    print(src.crs)
    print(src.transform)
    print(src.count)
    print(src.indexes)

## Plotting three color bands and its histogram
with rasterio.open('data/RGB.byte.tif') as src:
    fig, (axrgb, axhist) = plt.subplots(1, 2, figsize=(14,7))
    show(src, ax=axrgb)
    show_hist(src, bins=50, histtype='stepfilled',
          lw=0.0, stacked=False, alpha=0.3, ax=axhist)
    plt.show()



## Plotting three color bands
with rasterio.open('data/RGB.byte.tif') as src:
    fig, (axr, axg, axb) = plt.subplots(1,3, figsize=(21,7))
    show((src, 1), ax=axr, cmap='Reds', title='red channel')
    show((src, 2), ax=axg, cmap='Greens', title='green channel')
    show((src, 3), ax=axb, cmap='Blues', title='blue channel')
    plt.show()

## Plotting countours
with rasterio.open('data/RGB.byte.tif') as src:
    fig, ax = plt.subplots(1, figsize=(12, 12))
    show((src, 1), cmap='Greys_r', interpolation='none', ax=ax)
    show((src, 1), contour=True, ax=ax)
    plt.show()


#A rasterio dataset also provides methods for getting read/write windows (like extended array slices) given georeferenced coordinates.
with rasterio.open('data/RGB.byte.tif') as src:
    window = src.window(*src.bounds)
    print(window)
    print(src.read(window=window).shape)

# Read raster bands directly to Numpy arrays.
with rasterio.open('data/RGB.byte.tif') as src:
    r, g, b = src.read()
    # Write the product as a raster band to a new 8-bit file. For
    # the new file's profile, we start with the meta attributes of
    # the source file, but then change the band count to 1, set the
    # dtype to uint8, and specify LZW compression.
    profile = src.profile
    profile.update(dtype=rasterio.uint8, count=1, compress='lzw')

# Combine arrays in place. Expecting that the sum will
# temporarily exceed the 8-bit integer range, initialize it as
# a 64-bit float (the numpy default) array. Adding other
# arrays to it in-place converts those arrays "up" and
# preserves the type of the total array.
total = np.zeros(r.shape)
#print(total.shape) #(718, 791)

for band in r, g, b:
    total += band

total /= 3

with rasterio.open('data/example-total.tif', 'w', **profile) as dst:
    dst.write(total.astype(rasterio.uint8), 1)

