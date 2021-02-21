
## install environment and package 
conda create -n Filters python=3
conda activate Filters
conda install -c menpo opencv3
conda install numpy scipy matplotlib sympy

## Run environment 
1. Open a terminal 
2. Run: 
conda activate Filters

## Run Scripts
cd src
python ParticleFilter.py
python KalmanFilter.py
python ExtendedKalmanFilter.py

