#https://www.earthdatascience.org/workshops/gis-open-source-python/open-lidar-raster-python/

import os
import numpy as np
import matplotlib.pyplot as plt
import rasterio as rio
from rasterio.plot import show
from rasterio.plot import show_hist
from rasterio.mask import mask
import earthpy.plot as ep

# define path to digital terrain model
#sjer_dtm_path = "data/spatial-vector-lidar/california/neon-soap-site/2013/lidar/SOAP_lidarDTM.tif"
sjer_dtm_path = "data/spatial-vector-lidar/california/neon-sjer-site/2013/lidar/SJER_lidarDSM.tif"

# open raster data
lidar_dem = rio.open(sjer_dtm_path)


# read in all of the data without specifying a band
with rio.open(sjer_dtm_path) as src:
    print(src.bounds) # optional - view spatial extent
    lidar_dem_im = src.read(masked= True) # convert / read the data into a numpy array:
    #print(lidar_dem_im.shape) #(1, 1516, 3292)

# specify a band so you get a 2 dimensional image array
with rio.open(sjer_dtm_path) as src:
    lidar_dem_im = src.read(1, masked= True) # convert / read the data into a numpy array:
    sjer_ext = rio.plot.plotting_extent(src)
    print(lidar_dem_im.shape) #(1516, 3292)
    print(sjer_ext)

ep.plot_bands(lidar_dem_im,
              cmap='viridis_r',
              extent=sjer_ext,
              title="Lidar Digital Elevation Model \n Pre 2013 Boulder Flood | Lee Hill Road",
              scale=False)
plt.show()

# create histogram of data
ep.hist(lidar_dem_im,
        bins=100,
        title="Lee Hill Road - Digital Elevation (terrain) Model - \nDistribution of Elevation Values")
plt.show()


