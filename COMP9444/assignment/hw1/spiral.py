# spiral.py
# COMP9444, CSE, UNSW

import torch
import torch.nn as nn
import matplotlib.pyplot as plt


class PolarNet(torch.nn.Module):
    def __init__(self, num_hid):
        super(PolarNet, self).__init__()
        # INSERT CODE HERE
        self.layer1 = nn.Linear(2, num_hid)
        self.layer2 = nn.Linear(num_hid, 1)

    def forward(self, input):
        x = input[:, 0]
        y = input[:, 1]
        r = torch.sqrt(x ** 2 + y ** 2).reshape(-1, 1)
        a = torch.atan2(y, x).reshape(-1, 1)
        new_input = torch.cat((r, a), 1)
        self.hidden1 = torch.tanh(self.layer1(new_input))
        output = torch.sigmoid(self.layer2(self.hidden1))  # CHANGE CODE HERE
        return output


class RawNet(torch.nn.Module):
    def __init__(self, num_hid):
        super(RawNet, self).__init__()
        # INSERT CODE HERE
        self.layer1 = nn.Linear(2, num_hid)
        self.layer2 = nn.Linear(num_hid, num_hid)
        self.layer3 = nn.Linear(num_hid, 1)

    def forward(self, input):
        self.hid1 = torch.tanh(self.layer1(input))
        self.hid2 = torch.tanh(self.layer2(self.hid1))
        output = torch.sigmoid(self.layer3(self.hid2))  # CHANGE CODE HERE
        return output


def graph_hidden(net, layer, node):
    # modify the graph_output function
    xrange = torch.arange(start=-7, end=7.1, step=0.01, dtype=torch.float32)
    yrange = torch.arange(start=-6.6, end=6.7, step=0.01, dtype=torch.float32)
    xcoord = xrange.repeat(yrange.size()[0])
    ycoord = torch.repeat_interleave(yrange, xrange.size()[0], dim=0)
    grid = torch.cat((xcoord.unsqueeze(1), ycoord.unsqueeze(1)), 1)

    with torch.no_grad():  # suppress updating of gradients
        net.eval()  # toggle batch norm, dropout
        output = net(grid)
        # plot function computed by model
        if layer == 1:
            pred = (net.hidden1[:, node] >= 0).float()
        else:
            pred = (net.hidden2[:, node] >= 0).float()

        plt.clf()
        plt.pcolormesh(xrange, yrange, pred.cpu().view(yrange.size()[0], xrange.size()[0]), cmap='Wistia')
    # INSERT CODE HERE
