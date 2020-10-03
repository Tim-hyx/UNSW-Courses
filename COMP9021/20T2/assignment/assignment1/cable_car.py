import os.path
import sys

from collections import defaultdict

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
            if not line.split():
                continue
            line = ' '.join(line.split())
            for i in line.split(' '):
                lines.append(int(i))
        if len(lines) <= 1 or lines != sorted(lines):
            raise ValueError
        for i in lines:
            if not str(i).isdigit():
                raise ValueError
            if i <= 0:
                raise ValueError
except ValueError:
    print('Sorry, input file does not store valid data.')
    sys.exit()
    # modify the try except functions from quiz3

new_lines = [lines[i + 1] - lines[i] for i in range(len(lines) - 1)]  # find the gap of the list
length, n = 0, 0
while n <= len(new_lines) - 2:
    j, new_length = n + 1, 1
    # find the longest gap
    while j < len(new_lines) and new_lines[j] == new_lines[n]:
        j += 1
        new_length += 1
    if length < new_length:
        length = new_length
    n += 1

records, i, values = [], 1, 0
while i <= len(lines) - 1:
    j = i - 1
    records.append({})
    while j >= 0:
        value, num, num_gap = 0, 0, lines[i] - lines[j]
        for k in records[j - 1]:
            if k == num_gap:
                value, num = 1, records[j - 1][k]
        if value:
            records[i - 1][num_gap] = num + 1
        elif value == 0:
            records[i - 1][num_gap] = 1
        j -= 1
    i += 1
values = [max(i.values()) for i in records if values < max(i.values())]
remove = len(lines) - max(values) - 1

if len(lines) != max(values) + 1:
    print('The ride could be better...')
else:
    print('The ride is perfect!')
print(f'The longest good ride has a length of: {length}')
print(f'The minimal number of pillars to remove to build a perfect ride from the rest is: {remove}')
# find each value's gap which is the values in front of this value and find the most appeared times
