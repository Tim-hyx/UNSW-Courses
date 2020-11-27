from fractions import Fraction

A, B = [Fraction(i) for i in input('A B: ').split()]
AY, AN = [Fraction(i) for i in input('Y N for A: ').split()]
BY, BN = [Fraction(i) for i in input('Y N for B: ').split()]
YA = AY * A / (AY * A + BY * B)
YB = BY * B / (AY * A + BY * B)
NA = AN * A / (AN * A + BN * B)
NB = BN * B / (AN * A + BN * B)
print(f'YA: {YA}\nYB: {YB}\nNA: {NA}\nNB: {NB}')
