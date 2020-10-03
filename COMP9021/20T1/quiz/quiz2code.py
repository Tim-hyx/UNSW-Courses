# Written by *** and Eric Martin for COMP9021


from random import seed, shuffle
import sys


# for_seed is meant to be an integer, length a strictly positive integer.
# length will not be large for most tests, but can be as large as 10_000_000.
def generate_permutation(for_seed, length):
    seed(for_seed)
    values = list(range(1, length + 1))
    shuffle(values)
    return values


def maps_to(values, x):
    return values.index(x) + 1
    # REPLACE PASS ABOVE WITH YOUR CODE


def length_of_cycle_containing(values, x):
    c = values.index(x) + 1
    n = 1
    while c != x:
        n = n + 1
        c = values.index(c) + 1
    return n


# REPLACE PASS ABOVE WITH YOUR CODE


# Returns a list of length len(values) + 1, with 0 at index 0
# and for all x in {1, ..., len(values)}, the length of the cycle
# containing x at index x.
def analyse(values):
    list = [0] * (len(values) + 1)
    for i in range(1, len(values) + 1):
        if list[i] == 0:
            a = i
            b = [i]
            while values.index(a) + 1 != i:
                a = values.index(a) + 1
                b.append(a)
            for n in b:
                list[n] = len(b)
    return list
    # REPLACE PASS ABOVE WITH YOUR CODE
