cd $HOME/repositories/mxochicale/code/playground/rasterio
mkdir -p data && cd data

#Download RBG.byte.tif and tif from googleapis
wget https://github.com/rasterio/rasterio/raw/main/tests/data/RGB.byte.tif
wget https://storage.googleapis.com/gcp-public-data-landsat/LC08/01/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF

#Download spatial-vector-lidar data subset (~172 MB)
wget https://ndownloader.figshare.com/files/12459464 -O spatial-vector-lidar.zip


