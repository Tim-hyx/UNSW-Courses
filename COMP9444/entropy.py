from math import log
from fractions import Fraction

loop = True
while loop:
    print('Both float and fraction are supported (if there is no q,press enter)')
    p = [Fraction(pi) for pi in input('distribution p: ').split()]
    if sum(p) != 1:
        print('invalid distribution p')
        continue
    q = [Fraction(qi) for qi in input('distribution q: ').split()]
    if q and sum(q) != 1:
        print('invalid distribution q')
        continue
    Hp, loop = sum([pi * (-1 * log(pi, 2)) for pi in p]), False
    if q: Hq, DKLpq, DKLqp = sum([qi * (-1 * log(qi, 2)) for qi in q]), sum(
        [pi * (log(pi, 2) - log(qi, 2)) for (pi, qi) in zip(p, q)]), sum(
        [qi * (log(qi, 2) - log(pi, 2)) for (pi, qi) in zip(p, q)])
    print('H(p):', Hp, '\nH(q):', Hq, '\nDKL(p||q):', DKLpq, '\nDKL(q||p):', DKLqp) if q else print('H(p):', Hp)
