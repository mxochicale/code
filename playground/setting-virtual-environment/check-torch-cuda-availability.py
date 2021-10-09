# conda activate playground-ve-cpu
# conda activate playground-ve-gpu
# python check-torch-cuda-availability.py
import torch
print(torch.cuda.is_available())
