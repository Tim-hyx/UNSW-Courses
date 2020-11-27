import torch

Prob = torch.nn.functional.softmax(torch.tensor([float(z) for z in input('input Z: ').split()]).double(), dim=-1)
i = int(input('input i: '))
logProb = Prob * (-1)
logProb[i - 1] += 1
print(f'Prob:              {Prob}')
print(f'd(log Prob({i})/dz): {logProb}')
