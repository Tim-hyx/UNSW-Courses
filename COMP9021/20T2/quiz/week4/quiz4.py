# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Generates a list L of random nonnegative integers and prints out:
# - a list "fractions" of strings of the form 'a/b' such that:
#   . a <= b,
#   . a*n and b*n both occur in L for some n, and
#   . a/b is in reduced form
# enumerated from smallest fraction to largest fraction
#  (0 and 1 are exceptions, being represented as such rather than as
# 0/1 and 1/1);
# - if "fractions" contains 1/2, then the fact that 1/2 belongs to "fractions";
# - otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
#  if that member is unique;
# - otherwise, the two members "closest_1" and "closest_2" of "fractions" that
# are closest to 1/2, in their natural order.


import sys
from random import seed, randint
from math import gcd
from fractions import Fraction

try:
    arg_for_seed, length, max_value = (int(x) for x in
                                       input('Enter three nonnegative integers: ').split()
                                       )
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
spot_on, closest_1, closest_2 = [None] * 3

# INSERT YOUR CODE HERE
L = sorted(set(L))
for i in L:
    for j in L[-1:L.index(i):-1]:
        fractions.append(Fraction(i, j))
fractions.append(Fraction(1, 1))
fractions.sort()
if len(fractions) == 1:
    closest_1 = fractions[0]
gap = [abs(i - Fraction(1, 2)) for i in fractions]
gap.sort()
if Fraction(1, 2) in fractions:
    spot_on = True
else:
    if len(gap) > 1:
        if gap[0] == gap[1]:
            closest_1 = Fraction(1, 2) - gap[0]
            closest_2 = Fraction(1, 2) + gap[0]
        else:
            if (Fraction(1, 2) - gap[0]) in fractions:
                closest_1 = Fraction(1, 2) - gap[0]
            if Fraction(1, 2) + gap[0] in fractions:
                closest_1 = Fraction(1, 2) + gap[0]
fractions = [str(i) for i in fractions]
print('\nThe fractions no greater than 1 that can be built from L, '
      'from smallest to largest, are:'
      )
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')
