# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


from random import seed, randrange, sample
import sys
from os import path
from collections import defaultdict

try:
    for_seed, upper_bound, size = \
        (int(x) for x in input('Enter three nonnegative integers: ').split())
    if for_seed < 0 or upper_bound < 0 or size < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
w = len(str(upper_bound - 1))
with open('mapping.txt', 'w') as mapping:
    for (a, b) in zip(sorted(randrange(upper_bound) for _ in range(size)),
                      (randrange(upper_bound) for _ in range(size))
                      ):
        print(f'{a:{w}}', '->', b, file=mapping)
print('Here is the mapping that has been generated:')
with open('mapping.txt') as mapping:
    for line in mapping:
        print(line, end='')

valid_mapping = True
most_frequent_inputs = []
function = {}

# INSERT YOUR CODE HERE
dirt1, dirt2, num = defaultdict(int), {}, []
with open('mapping.txt') as mapping:
    lines = [line for line in mapping]
    if len(set(lines)) != len(lines):
        valid_mapping = False
    if len(set(lines)) == len(lines):
        i = 0
        while i < len(lines):
            line = lines[i]
            num = [item.strip() for item in line.split('->')]
            input, output = int(num[0]), int(num[1])
            dirt2[input] = output
            dirt1[input] += 1
            i += 1
        for k, v in dirt1.items():
            if v == 1:
                function[k] = dirt2[k]
        max = max(dirt1.values())
        most_frequent_inputs = [k for k, v in dirt1.items() if v == max]
if not valid_mapping:
    print("Sorry, that's not a correct mapping.")
else:
    print("Ok, that's a correct mapping.")
    print('The list of most frequent inputs is:\n\t', most_frequent_inputs)
    print('The function extracted from the mapping is:\n\t', function)
