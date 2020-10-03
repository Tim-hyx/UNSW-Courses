# Returns the product of the prime factors of n whose multiplicity
# (the power of the factor in the decomposition of n as prime factors)
# is maximal.
#
# The sample tests show the prime decomposition of inputs and
# outputs, so provide illustrative examples.
#
# You will pass all tests if, writing the prime decomposition of
# n as p_1**k_1 * p_2**k_2 * ... * p_n**k_n, your solution is linear
# in p_n + k_1 + k_2 + ... + k_n (so linear in the sum of the largest
# prime factor and the multiplicities of all prime factors).
#
# You can assume that $n$ is an integer at least equal to 2.


from collections import defaultdict
import math
from math import gcd


def isprime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


def maxPrimeFactor(n):
    # number must be even
    while n % 2 == 0:
        max_Prime = 2
        n /= 1
    # number must be odd
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_Prime = i
            n = n / i
    # prime number greator than two
    if n > 2:
        max_Prime = n
    return int(max_Prime)


def factorization(n):
    factors = []
    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1
        while factor == 1:
            for count in range(cycle_size):
                if factor > 1:
                    break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)

            cycle_size *= 2
            x_fixed = x

        return factor
    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next

    return factors


def f(n):
    '''
    >>> # 7**34
    >>> f(54116956037952111668959660849)
    54116956037952111668959660849
    >>> # 31**8 * 67**8
    >>> f(346331482782541014529195681)
    346331482782541014529195681
    >>> # Input: 23 * 41**2 * 107**3 * 277 * 601**2 * 941**3
    >>> # Output: 107**3 * 941**3
    >>> f(3948612043999200544581190253)
    1020751914942703
    >>> # Input: 43**9 * 101**8 * 163**9, output: 43**9 * 163**9
    >>> f(442054209072932552970016977855829514295893682554689)
    40822964550654154780091961646843489
    >>> # Input: 257**3 * 467**5 * 739**2 * 881**5 * 977**5
    >>> # Output = 467**5 * 881**5 * 977**5
    >>> f(97280324422048553955452584856846119473179701956041921947)
    10493896185731177369522700530133883393416899
    
    '''
    n2 = factorization(n)
    max_mul = 0
    all_fac = []
    for i in n2:
        temp = maxPrimeFactor(i)
        max_mul = max(max_mul, temp)
        if isprime(i):
            all_fac.append(i)
        else:
            all_fac.append(temp)
    max_expo = 0
    a1 = n
    while a1 % max_mul == 0:
        a1 = a1 // max_mul
        max_expo += 1
    all_fac = set(all_fac)
    final = []
    for i in all_fac:
        max_expo2 = 0
        a2 = n
        while a2 % i == 0:
            a2 = a2 // i
            max_expo2 += 1
        if max_expo2 == max_expo:
            final.append(i)
    result = 1
    for i in final:
        result *= i ** max_expo
    return result
# REPLACE return 1 ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
