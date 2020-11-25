# kuzu.py
# COMP9444, CSE, UNSW

from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F


class NetLin(nn.Module):
    # linear function followed by log_softmax
    def __init__(self):
        super(NetLin, self).__init__()
        # INSERT CODE HERE
        self.layer = nn.Linear(28 * 28, 10)

    def forward(self, x):
        x = x.view(x.shape[0], -1)
        return F.log_softmax(self.layer(x), dim=1)  # CHANGE CODE HERE


class NetFull(nn.Module):
    # two fully connected tanh layers followed by log softmax
    def __init__(self):
        super(NetFull, self).__init__()
        # INSERT CODE HERE
        self.layer1 = nn.Linear(28 * 28, 210)
        self.layer2 = nn.Linear(210, 10)

    def forward(self, x):
        x = torch.tanh(self.layer1(x.view(x.shape[0], -1)))
        return F.log_softmax(self.layer2(x), dim=1)  # CHANGE CODE HERE


class NetConv(nn.Module):
    # two convolutional layers and one fully connected layer,
    # all using relu, followed by log_softmax
    def __init__(self):
        super(NetConv, self).__init__()
        # INSERT CODE HERE
        self.conv1 = nn.Conv2d(1, 16, 5, padding=2)
        self.conv2 = nn.Conv2d(16, 32, 5, padding=2)
        self.pool = nn.MaxPool2d(5, padding=2)
        self.layer1 = nn.Linear(1152, 600)
        self.layer2 = nn.Linear(600, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = x.view(x.shape[0], -1)
        return F.log_softmax(self.layer2(F.relu(self.layer1(x))), dim=1)  # CHANGE CODE HERE
