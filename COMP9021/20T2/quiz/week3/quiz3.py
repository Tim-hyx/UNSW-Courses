# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Call multibase a nonempty finite sequence of strictly positive
# integers (a_n, ..., a_0) all at most equal to 10.
# A positive integer is said to be a valid representation in the
# multibase if it is of the form x_k...x_0 with k <= n and for all
# i in {0,...,k}, x_i < a_i. Its representation in base 10 is defined as
# x_0 + x_1*a_0 + x_2*a_0*a_1 + ... + x_k*a_0*a_1*...*a_{k-1}.
#
# Determines the largest integer with a valid representation
# in the multibase, and converts representations between base
# 10 and the multibase.
#
# For instance, consider the multibase (8, 10, 6, 1).
# - 3820 is a valid representation in the multibase; it is the number
#   that in base 10 reads as 0 + 2*1 + 8*6*1 + 3*10*6*1 = 230.
# - 432, as a decimal number, can be represented in the multibase,
#   reading as 7200, since 2*6 + 7*10*6 = 432.

import sys

try:
    multibase = [int(x) for x in input('Enter a nonempty sequence of integers '
                                       'between 1 and 10: '
                                       ).split()
                 ]
    if not len(multibase) or any(b < 1 or b > 10 for b in multibase):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    input_multibase_representation = \
        int(input('Enter a first positive number: '))
    if input_multibase_representation < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    input_base_10_representation = \
        int(input('Enter a second positive number: '))
    if input_base_10_representation < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

valid_multibase_representation = True
valid_base_10_representation = True
max_number = 0
output_multibase_representation = 0
output_base_10_representation = 0

# INSERT YOUR CODE HERE
max_number += 1
for i in multibase:
    max_number *= i
max_number -= 1
if input_base_10_representation > max_number:
    valid_base_10_representation = False
multibase.reverse()
real_multibase = [1]
i = 0
while i < len(multibase):
    num, last = multibase[i], real_multibase[-1]
    real_multibase.append(last * num)  # real_multibase= [1 1 6 60 480]
    i += 1

# 万     千      百      十      个
# 8     10      6       1
# 480   60      6       1       1
#       3       8       2       0
# 3820
# 3*60 + 6*8 + 2*1 + 1*0 = 230
if len(str(input_multibase_representation)) >= len(real_multibase):
    valid_multibase_representation = False
else:
    first = input_multibase_representation
    j = 0
    while j < len(real_multibase) - 1:
        first, remain = divmod(first, 10)  # get remain
        x = real_multibase[j]
        output_base_10_representation += remain * x  # 3*60 + 6*8 + 2*1 + 1*0 = 230
        if remain >= multibase[j]:
            valid_multibase_representation = False
            break
        j += 1

# 432
#                                商          余数
# 对万位求商和余数：432 % 480       0           432 （万位）
# 对千位求商和余数：432 % 60        7           12  （千位）
# 对百位求商和余数：12 %  6         2           0   （百位）
# 对十位求商和余数：0 %   1         0           0   （十位）
# 对个位求商和余数：0 %   1         0           0   （个位）
if input_base_10_representation <= max_number:
    second = input_base_10_representation
    real_multibase.reverse()  # real_multibase= [480 60 6 1 1]
    n = 0
    while n < len(real_multibase):
        j = real_multibase[n]
        a, second = divmod(second, j)  # get quotient
        output_multibase_representation = output_multibase_representation * 10 + a  # 7*1000 + 2*100 + 0*10 + 0*1 = 7200
        n += 1
print('The largest number that can be represented in this multibase is:',
      max_number
      )
if not valid_multibase_representation:
    print(input_multibase_representation,
          'is not a valid representation in the given multibase.'
          )
else:
    print('In base 10,', input_multibase_representation,
          'reads as:', output_base_10_representation
          )
if not valid_base_10_representation:
    print(input_base_10_representation, 'cannot be represented in the '
                                        'given multibase.'
          )
else:
    print('In the given multibase,', input_base_10_representation,
          'reads as:', output_multibase_representation
          )
