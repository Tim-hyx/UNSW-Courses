from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
import sys

# Insert your code here
try:
    arg_for_seed = int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
# Prompts the user a strictly positive number, nb_of_elements.
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
seed(arg_for_seed)
# Generates a list of nb_of_elements random integers between 0 and 99.
L = [randint(-50, 50) for _ in range(nb_of_elements)]
# Prints out the list.
print('\nThe list is:', L)
print()
the_mean = sum(L) / nb_of_elements
L = sorted(L)
the_median = L[0]
if len(L) > 1:
    if len(L) % 2 == 1:
        the_median = L[int(len(L) / 2)]
    else:
        the_median = (L[int((len(L) + 1) / 2)] + L[int((len(L) + 1) / 2 - 1)]) / 2
sum_num = 0
for j in L:
    sum_num += j ** 2
standard_deviation = sqrt(sum_num / nb_of_elements - the_mean ** 2)
print('The mean is %.2f.' % the_mean)
print('The median is %.2f.' % the_median)
print('The standard deviation is %.2f.' % standard_deviation)
print()
print('Confirming with functions from the statistics module:')
print('The mean is %.2f.' % mean(L))
print('The median is %.2f.' % median(L))
print('The standard deviation is %.2f.' % pstdev(L))

