#https://www.earthdatascience.org/workshops/gis-open-source-python/crop-raster-data-in-python/

import os
import numpy as np
import rasterio as rio
from rasterio.plot import show
from rasterio.mask import mask
import matplotlib.pyplot as plt
import earthpy as et
import earthpy.plot as ep
import earthpy.spatial as es
import geopandas as gpd

soap_chm_path = 'data/spatial-vector-lidar/california/neon-soap-site/2013/lidar/SOAP_lidarCHM.tif'

# open the lidar chm
with rio.open(soap_chm_path) as src:
    lidar_chm_im = src.read(masked=True)[0]
    extent = rio.plot.plotting_extent(src)
    soap_profile = src.profile

#print(type(lidar_chm_im))
#<class 'numpy.ma.core.MaskedArray'>

#ep.plot_bands(lidar_chm_im,
#               cmap='terrain',
#               extent=extent,
#               title="Lidar Canopy Height Model (CHM)\n NEON SOAP Field Site",
#               cbar=False);
#

#Open Vector Layer
crop_extent_soap = gpd.read_file('data/spatial-vector-lidar/california/neon-soap-site/vector_data/SOAP_crop2.shp')

#explore the coordinate reference system (CRS)
print('crop extent crs: ', crop_extent_soap.crs)
print('lidar crs: ', soap_profile['crs'])

# plot the data
fig, ax = plt.subplots(figsize = (6, 6))
crop_extent_soap.plot(ax=ax)
ax.set_title("Shapefile Imported into Python \nCrop Extent for Soaproot Saddle Field Site", 
             fontsize = 16)
ax.set_axis_off()
plt.show()

fig, ax = plt.subplots(figsize=(10, 10))
ep.plot_bands(lidar_chm_im,
              cmap='terrain',
              extent=extent,
              ax=ax,
              cbar=False)
crop_extent_soap.plot(ax=ax, alpha=.6, color='g');
plt.show()

#To crop the data,use the crop_image function in earthpy.spatial.
with rio.open(soap_chm_path) as src:
    lidar_chm_crop, soap_lidar_meta = es.crop_image(src, crop_extent_soap)

# Update the metadata to have the new shape (x and y and affine information)
soap_lidar_meta.update({"driver": "GTiff",
                 "height": lidar_chm_crop.shape[0],
                 "width": lidar_chm_crop.shape[1],
                 "transform": soap_lidar_meta["transform"]})

# generate an extent for the newly cropped object for plotting
cr_ext = rio.transform.array_bounds(soap_lidar_meta['height'], 
                                            soap_lidar_meta['width'], 
                                            soap_lidar_meta['transform'])

bound_order = [0,2,1,3]
cr_extent = [cr_ext[b] for b in bound_order]
cr_extent, crop_extent_soap.total_bounds

# mask the nodata and plot the newly cropped raster layer
lidar_chm_crop_ma = np.ma.masked_equal(lidar_chm_crop[0], -9999.0) 
# plot
ep.plot_bands(lidar_chm_crop_ma, cmap='terrain', cbar=False)


