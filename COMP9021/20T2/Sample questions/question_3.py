from math import log, ceil, sqrt


# Prints out all lines of the form k = b^p such that:
# - m <= k <= n
# - p >= 2
# from smallest k to largest k and for a given k,
# from smallest b to largest b.
#
# No indication on the range of values to be tested,
# just do your best...
#
# You can assume that m and n are positive integers.
def f(m, n):
    '''
    >>> f(10000, 1)
    >>> f(17, 21)
    >>> f(17, 210)
    25 = 5^2
    27 = 3^3
    32 = 2^5
    36 = 6^2
    49 = 7^2
    64 = 2^6
    64 = 4^3
    64 = 8^2
    81 = 3^4
    81 = 9^2
    100 = 10^2
    121 = 11^2
    125 = 5^3
    128 = 2^7
    144 = 12^2
    169 = 13^2
    196 = 14^2
    >>> f(110500, 117700)
    110592 = 48^3
    110889 = 333^2
    111556 = 334^2
    112225 = 335^2
    112896 = 336^2
    113569 = 337^2
    114244 = 338^2
    114921 = 339^2
    115600 = 340^2
    116281 = 341^2
    116964 = 342^2
    117649 = 7^6
    117649 = 49^3
    117649 = 343^2
    >>> f(34359738368, 34359848368)
    34359738368 = 2^35
    34359738368 = 32^7
    34359738368 = 128^5
    34359812496 = 185364^2
    34359822251 = 3251^3
    '''
    if n < m:
        return
    else:
        find_max_p = 2
        while pow(2, find_max_p) <= n:
            find_max_p += 1
        find_max_b = ceil(sqrt(n))
        print_list = []
        for p in range(2, find_max_p):
            for b in range(2, find_max_b):
                k = b ** p
                if m <= k <= n:
                    print_list.append([k, b, p])
        print_list.sort(key=lambda x: (x[0], x[1]))
        for i in range(len(print_list)):
            print(f'{print_list[i][0]} = {print_list[i][1]}^{print_list[i][2]}')
    # REPLACE PASS ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
