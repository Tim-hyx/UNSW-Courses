# Decodes all multiplications of the form
#
#                        *  *  *
#                   x       *  *
#                     ----------
#                     *  *  *  *
#                     *  *  *
#                     ----------
#                     *  *  *  *
#
# such that the sum of all digits in all 4 columns is constant.


for x in range(100, 1_000):
    for y in range(10, 100):
        a = str(y)
        b = str(x)
        product0 = x * int(a[1])
        c = str(product0)
        if product0 < 1000:
            continue
        product1 = x * int(a[0])
        d = str(product1)
        if product1 >= 1000:
            continue
        totalnumber = product0 + 10 * product1
        e = str(totalnumber)
        column = int(b[2]) + int(a[1]) + int(c[3]) + int(e[3])
        if int(b[1]) + int(a[0]) + int(c[2]) + int(e[2]) + int(d[2]) != column:
            continue
        if int(b[0]) + int(c[1]) + int(e[1]) + int(d[1]) != column:
            continue
        if int(c[0]) + int(e[0]) + int(d[0]) != column:
            continue
        print('A solution with all columns adding up to ' + str(column) + ':')
        print('      ', ' '.join(i for i in b))
        print('     ' + 'x' + '  ', ' '.join(i for i in a))
        print('     -------')
        print('    ', ' '.join(i for i in c))
        print('      ', ' '.join(i for i in d))
        print('     -------')
        print('    ', ' '.join(i for i in e))
        print()
        # Replace pass above with your code.
        # Compute the first partial product product0, namely, x * (y % 10),
        # and make sure it is at least equal to 1000.
        # Compute the second partial product product1 and make sure it is smaller than 1000.
        # Perform all other necessary tests...
