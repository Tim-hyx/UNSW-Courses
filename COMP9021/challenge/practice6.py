# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial


# Insert your code here
def first_computation(x):
    number = 0
    while x % 10 == 0:
        number += 1
        x //= 10
    return number
    # Replace pass above with your code


def second_computation(x):
    for i in range(1, len(x)):
        if x[-i] == '0':
            continue
        else:
            return i - 1
    # Replace pass above with your code


def third_computation(x):
    a = 0
    b = 5
    while x >= b:
        a += x // b
        b *= 5
    return a
    # Replace pass above with your code


try:
    the_input = int(input('Input a nonnegative integer: '))
    if the_input < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

the_input_factorial = factorial(the_input)
print(f'Computing the number of trailing 0s in {the_input}! by dividing by 10 for long enough:',
      first_computation(the_input_factorial))
print(f'Computing the number of trailing 0s in {the_input}! by converting it into a string:',
      second_computation(str(the_input_factorial)))
print(f'Computing the number of trailing 0s in {the_input}! the smart way:',
      third_computation(the_input))
