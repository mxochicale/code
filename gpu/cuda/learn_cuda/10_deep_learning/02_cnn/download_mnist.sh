#!/bin/sh

url_base=http://yann.lecun.com/exdb/mnist

mkdir -p dataset
cd dataset

curl -O ${url_base}/train-images-idx3-ubyte.gz
curl -O ${url_base}/train-labels-idx1-ubyte.gz
curl -O ${url_base}/t10k-images-idx3-ubyte.gz
curl -O ${url_base}/t10k-labels-idx1-ubyte.gz

#gunzip *.gz


#Its simple, I had the similar problem while ago, what I did was just rename the file.
#that is to remove the .gz from the file name. Then it looks like access.log. So you can view it using any editor you have
#https://askubuntu.com/questions/715925/gzip-file-log-gz-not-in-gzip-format-error
mv train-images-idx3-ubyte.gz train-images-idx3-ubyte
mv train-labels-idx1-ubyte.gz train-labels-idx1-ubyte
mv t10k-images-idx3-ubyte.gz t10k-images-idx3-ubyte
mv t10k-labels-idx1-ubyte.gz t10k-labels-idx1-ubyte



