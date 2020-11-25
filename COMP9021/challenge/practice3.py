from random import seed, randrange
import sys


# Insert your code here
from random import seed, randrange
import sys
try:
    arg_for_seed = int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
seed(arg_for_seed)
L = [randrange(20) for _ in range(nb_of_elements)]
print('\nThe list is:' , L)
print()
remainders_modulo_5 = [0] * 4
for e in L:
    remainders_modulo_5[e // 5] += 1
for i in range(4):
    if remainders_modulo_5[i] == 0:
        print('There is no element', end=' ')
    elif remainders_modulo_5[i] == 1:
        print('There is 1 element', end=' ')
    else:
        print(f'There are', remainders_modulo_5[i], 'elements', end=' ')
    print(f'between {i*5} and {i*5+4}.')