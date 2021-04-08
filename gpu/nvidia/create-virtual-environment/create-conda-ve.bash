#!/bin/bash

conda deactivate
conda env create --file env.yml  

conda activate ve-python38-cuda11
