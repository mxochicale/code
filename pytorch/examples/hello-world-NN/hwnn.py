"""Reference: https://www.digitalocean.com/community/tutorials/introduction-to-pytorch-build-a-neural-network-to-recognize-handwritten-digits"""

import torch
import torch.nn as nn
import torch.optim as optim

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
if device.type == 'cuda':
    print("Is cuda available: ", torch.cuda.is_available())
    print("Number of devices: ", torch.cuda.device_count())
    print("Name of the device(0): ", torch.cuda.get_device_name(0))

net = nn.Linear(1, 1)  # 1. Build a computation graph (a line!)
optimizer = optim.SGD(net.parameters(), lr=0.1)  # 2. Setup optimizers
criterion = nn.MSELoss()  # 3. Setup criterion
x, target = torch.randn((1,)), torch.tensor([0.])  # 4. Setup data

# 5. Train the model
for i in range(10):
    output = net(x)
    loss = criterion(output, target)
    print("  loss", round(loss.item(), 3))
    net.zero_grad()
    loss.backward()
    optimizer.step()
