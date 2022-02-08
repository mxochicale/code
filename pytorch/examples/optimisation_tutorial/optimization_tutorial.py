# Reference
# https://github.com/pytorch/tutorials/blob/master/beginner_source/basics/optimization_tutorial.py
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


########################################
# .. _full-impl-label:
#
# Full Implementation
# -----------------------
# We define ``train_loop`` that loops over our optimization code, and
# ``test_loop`` that evaluates the model's performance against our test data.

def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)

    for batch, (X, y) in enumerate(dataloader):
        # print(X.size()) #torch.Size([64, 1, 28, 28]); torch.Size([32, 1, 28, 28])
        # print(y.size()) #torch.Size([64]); torch.Size([32])

        # Compute prediction and loss
        pred = model(X)  # print(pred.size())#torch.Size([64, 10]); torch.Size([32, 10])
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def test_loop(dataloader, model, loss_fn):
    size = len(dataloader.dataset)  # print(size) # 10000
    num_batches = len(dataloader)  # print(num_batches) # 157
    test_loss, correct = 0, 0

    with torch.no_grad():
        for batch, (X, y) in enumerate(dataloader):
            # print(batch)
            # print(X.size()) #torch.Size([16, 1, 28, 28])
            # print(y.size()) #torch.Size([16])
            pred = model(X)  #
            # print(pred.size())  # torch.Size([64, 10]) # torch.Size([16, 10])
            test_loss += loss_fn(pred, y).item()
            # print(pred.argmax(1)==y)
            # print(y)
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100 * correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")


# Hyperparameters
# ---------------
learning_rate = 1e-3
batch_size = 32
epochs = 2

# Create model
# ---------------
model = NeuralNetwork()

# Create train and test dataloaders
# ---------------
train_dataloader = DataLoader(training_data, batch_size=batch_size)  # len(train_dataloader) = 938; len(train_dataloader.dataset)=60000
test_dataloader = DataLoader(test_data, batch_size=batch_size)  # len(test_dataloader) = 157; len(test_dataloader.dataset)=10000

# We initialize the loss function and optimizer, and pass it to ``train_loop`` and ``test_loop``.
# Feel free to increase the number of epochs to track the model's improving performance.
# Initialize the loss function
loss_fn = nn.CrossEntropyLoss()
# Optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

for t in range(epochs):
    print(f"Epoch {t + 1}\n-------------------------------")
    train_loop(train_dataloader, model, loss_fn, optimizer)
    test_loop(test_dataloader, model, loss_fn)
print("Done!")
