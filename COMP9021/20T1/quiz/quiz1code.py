# Written by *** and Eric Martin for COMP9021
#
# Generates a random list of integers between 1 and 6
# whose length is chosen by the user, displays the list,
# outputs the difference between last and first values,
# then displays the values as horizontal bars of stars,
# then displays the values as vertical bars of stars
# surrounded by a frame.


from random import seed, randrange
import sys
            

try:
    for_seed, length = (int(x) for x in input('Enter two integers, the second '
                                              'one being strictly positive: '
                                             ).split()
                       )
    if length <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(1, 7) for _ in range(length)]
print('Here are the generated values:', values)
# INSERT CODE HERE
print('')
print('The difference between last and first values is:\n  ',values[-1]-values[0])
print('')
print('Here are the values represented as horizontal bars:')
# INSERT CODE HERE
print('')
a = []
for i in range(len(values)):
    a.append([0 for i in range(max(values))])
for n in range(len(values)):
    for i in range(values[n]):
        a[n][i] = 1
    print('  ','  *' * values[n],'')
print('')
print('Here are the values represented as vertical bars, '
      'with a surrounding frame:'
     )
# INSERT CODE HERE
print('')
print('   '+'-'*(3*len(values)+2))
for i in range(-1, -len(a[0]) - 1, -1):
    b = ''
    for j in range(len(a)):
        if a[j][i] == 1 and j>0:
            b = b + "  *"
        elif a[j][i] == 1 and j==0:
            b = b + " *"
        elif a[j][i] == 0 and j==0:
            b = b + "  "
        else:
            b = b + "   "
    b = "|" + b + " |"
    print('  ',b)
print('   '+'-'*(3*len(values)+2))
print('')
