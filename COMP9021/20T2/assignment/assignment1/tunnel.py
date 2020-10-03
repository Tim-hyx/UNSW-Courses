import os.path
import sys
from collections import deque

try:
    file_name = input('Please enter the name of the file you want to get data from: ')
    if not os.path.exists(file_name):
        raise FileNotFoundError
except FileNotFoundError:
    print('Sorry, there is no such file.')
    sys.exit()
try:
    with open(file_name) as open_file:
        lines = []
        for line in open_file:
            two_line = []
            if not line.split():
                continue
            line = ' '.join(line.split())
            for n in line.split():
                two_line.append(int(n))
            lines.append(two_line)
        if len(lines) != 2:
            raise ValueError
        ceiling, floor = lines[0], lines[1]
        if len(ceiling) != len(floor) or len(ceiling) < 2 or len(floor) < 2:
            raise ValueError
        for n in ceiling:
            if not str(n).isdigit():
                raise ValueError
        for n in floor:
            if not str(n).isdigit():
                raise ValueError
        for n in range(len(ceiling)):
            if ceiling[n] <= floor[n]:
                raise ValueError
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()
# modify the try except functions from Q2

max_depth, i = 1, 0
while i <= ceiling[0] - floor[0] - 1:
    depth, j = 1, 1
    while j <= len(floor) - 1:
        if (floor[0] + i) >= ceiling[j]:
            break
        elif (floor[0] + i) < floor[j]:
            break
        else:
            depth += 1
            if depth > max_depth:
                max_depth = depth
        j += 1
    i += 1
print(f'From the west, one can into the tunnel over a distance of {max_depth}')
# use the first one,the final floor to find should lower than first ceiling, so every time +1,find others should lower
# than it,and +1 again

max_distance, i = 1, 0
while i <= len(ceiling) - 2:
    j = 0
    while j <= ceiling[i] - floor[i] - 1:
        distance, n = 1, i + 1
        while n <= len(ceiling) - 1:
            if (floor[i] + j) >= ceiling[n]:
                break
            elif (floor[i] + j) < floor[n]:
                break
            else:
                distance += 1
                if distance > max_distance:
                    max_distance = distance
            n += 1
        j += 1
    i += 1
print(f'Inside the tunnel, one can into the tunnel over a maximum distance of {max_distance}')
# find every floor's max distance,like floor+0,floor+1,floor+2.... and then go to the next floor also calculate its all
# max distance and so on, finally find the max distance
