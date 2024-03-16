#https://www.earthdatascience.org/workshops/gis-open-source-python/intro-vector-data-python/

import os
import matplotlib.pyplot as plt
import geopandas as gpd
import earthpy as et

sjer_plot_locations = gpd.read_file('data/spatial-vector-lidar/california/neon-sjer-site/vector_data/SJER_plot_centroids.shp')

#Shapefile Structure
#There are 3 key files associated with any and all shapefiles:
#.shp: the file that contains the geometry for all features.
#.shx: the file that indexes the geometry.
#.dbf: the file that stores feature attributes in a tabular format.


PRINT=True
#PRINT=False
if PRINT:
    # view  the top 6 lines of attribute table of data
    #print(sjer_plot_locations.head(6))
    print(sjer_plot_locations)
    #print(type(sjer_plot_locations)) #<class 'geopandas.geodataframe.GeoDataFrame'>

    #view the spatial extent
    #print(sjer_plot_locations.total_bounds) #[ 254738.618 4107527.074  258497.102 4112167.778]
    #The spatial extent of a shapefile or geopandas GeoDataFrame represents the geographic "edge" or 
    #location that is the furthest north, south east and west. 
    #Thus is represents the overall geographic coverage of the spatial object. 
    #Image Source: National Ecological Observatory Network (NEON)    
    #print(sjer_plot_locations.crs) #EPSG:32611
    #print(sjer_plot_locations.geom_type)
    #print(sjer_plot_locations.shape) #(18, 6)


## quickly plot the data adding a legend
fig, ax = plt.subplots(figsize = (10,10))
sjer_plot_locations.plot(column='plot_type', 
                         categorical=True, 
                         legend=True, 
                         figsize=(10,6),
                         marker='*', 
                         markersize=45, 
                         cmap="Set2", ax=ax);
ax.set_title('SJER Plot Locations\nMadera County, CA', fontsize=16);
plt.show()


