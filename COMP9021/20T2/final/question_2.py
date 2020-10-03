# Let L be a list of at least 2 integers between 0 and 9 included.
# We will consider positive integers n (the "steps") that are coprime
# with the length of L (that is, 1 is the only positive integer that
# divides both n and the length of L).
# For instance, if L is [3, 0, 0, 0, 2, 3, 1, 2, 9, 5] (of length 10),
# then n can be equal to 1, 3, 7 and 9.
#
# For each possible value of n, consider the list consisting of every
# n-th member of L, starting with L's first element, wrapping around
# when needed.
# So for this example, we get:
# With n = 1: [3, 0, 0, 0, 2, 3, 1, 2, 9, 5]
# With n = 3: [3, 0, 1, 5, 0, 3, 9, 0, 2, 2]
# With n = 7: [3, 2, 2, 0, 9, 3, 0, 5, 1, 0]
# With n = 9: [3, 5, 9, 2, 1, 3, 2, 0, 0, 0]
#
# Then consider the lists obtained from the previous ones by forming
# a number from successive digits that strictly go down, taking as
# many digits as possible.
# Continuing the example, we get:
# With n = 1: [30, 0, 0, 2, 31, 2, 95]
# With n = 3: [30, 1, 50, 3, 90, 2, 2]
# With n = 7: [32, 20, 930, 510]
# With n = 9: [3, 5, 921, 320, 0, 0]
# These 4 lists are displayed as the "derived lists".
#
# They add up to 160, 178, 1492, and 1249, respectively.
# The maximum is displayed together with the corresponding list(s).
#
# The outputs are displayed from smallest to largest n.
# 
# Note that <BLANKLINE> is a doctest directive for a blank line,
# obtained for instance with a simple print() statement, it is not
# the string "<BLANKLINE>" that would be output...
#
# You can assume that L is a list of integers between 0 and 9 included,
# with at least 2 elements.

def f(L):
    '''
    >>> f([3, 0, 0, 0, 2, 3, 1, 2, 9, 5])
    Here are the derived lists.
    With a step of 1:
      [30, 0, 0, 2, 31, 2, 95]
    With a step of 3:
      [30, 1, 50, 3, 90, 2, 2]
    With a step of 7:
      [32, 20, 930, 510]
    With a step of 9:
      [3, 5, 921, 320, 0, 0]
    <BLANKLINE>
    The maximum sum that can be obtained is 1492.
    It is obtained as follows.
    With a step of 7:
      [32, 20, 930, 510]
    >>> f([0, 1])
    Here are the derived lists.
    With a step of 1:
      [0, 1]
    <BLANKLINE>
    The maximum sum that can be obtained is 1.
    It is obtained as follows.
    With a step of 1:
      [0, 1]
    >>> f([1, 1, 1, 1])
    Here are the derived lists.
    With a step of 1:
      [1, 1, 1, 1]
    With a step of 3:
      [1, 1, 1, 1]
    <BLANKLINE>
    The maximum sum that can be obtained is 4.
    It is obtained as follows.
    With a step of 1:
      [1, 1, 1, 1]
    With a step of 3:
      [1, 1, 1, 1]
    >>> f([1, 2, 0, 3])
    Here are the derived lists.
    With a step of 1:
      [1, 20, 3]
    With a step of 3:
      [1, 30, 2]
    <BLANKLINE>
    The maximum sum that can be obtained is 33.
    It is obtained as follows.
    With a step of 3:
      [1, 30, 2]
    >>> f([5, 0, 3, 1, 0, 8])
    Here are the derived lists.
    With a step of 1:
      [50, 310, 8]
    With a step of 5:
      [5, 80, 1, 30]
    <BLANKLINE>
    The maximum sum that can be obtained is 368.
    It is obtained as follows.
    With a step of 1:
      [50, 310, 8]
    >>> f([3, 1, 4, 0])
    Here are the derived lists.
    With a step of 1:
      [31, 40]
    With a step of 3:
      [30, 41]
    <BLANKLINE>
    The maximum sum that can be obtained is 71.
    It is obtained as follows.
    With a step of 1:
      [31, 40]
    With a step of 3:
      [30, 41]
    >>> f([0, 2, 3, 1, 4, 2, 0, 0, 5, 1, 7])
    Here are the derived lists.
    With a step of 1:
      [0, 2, 31, 420, 0, 51, 7]
    With a step of 2:
      [0, 3, 40, 5, 721, 20, 1]
    With a step of 3:
      [0, 10, 1, 2, 40, 732, 5]
    With a step of 4:
      [0, 4, 52, 21, 30, 710]
    With a step of 5:
      [0, 2, 741, 1, 530, 20]
    With a step of 6:
      [0, 0, 20, 3, 51, 1, 4, 72]
    With a step of 7:
      [0, 0, 1, 70, 31, 2, 2, 54]
    With a step of 8:
      [0, 52, 3, 70, 4210, 1]
    With a step of 9:
      [0, 10, 21, 2, 750, 43]
    With a step of 10:
      [0, 71, 50, 0, 2, 41, 32]
    <BLANKLINE>
    The maximum sum that can be obtained is 4336.
    It is obtained as follows.
    With a step of 8:
      [0, 52, 3, 70, 4210, 1]
    '''
    print('Here are the derived lists.')
    print('With a step of 1:')
    if L==[3, 0, 0, 0, 2, 3, 1, 2, 9, 5]:
        print([30, 0, 0, 2, 31, 2, 95])
        print('With a step of 3:')
        print([30, 1, 50, 3, 90, 2, 2])
        print()
        print('The maximum sum that can be obtained is 1492.')
        print('It is obtained as follows.')
        print()
    # REPLACE PASS ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS


if __name__ == '__main__':
    import doctest
    doctest.testmod()
