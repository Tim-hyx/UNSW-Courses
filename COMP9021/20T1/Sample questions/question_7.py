'''
Will be tested with height a strictly positive integer.
'''


def f(height):
    '''
    >>> f(1)
    0
    >>> f(2)
     0
    123
    >>> f(3)
      0
     123
    45678
    >>> f(4)
       0
      123
     45678
    9012345
    >>> f(5)
        0
       123
      45678
     9012345
    678901234
    >>> f(6)
         0
        123
       45678
      9012345
     678901234
    56789012345
    >>> f(20)
                       0
                      123
                     45678
                    9012345
                   678901234
                  56789012345
                 6789012345678
                901234567890123
               45678901234567890
              1234567890123456789
             012345678901234567890
            12345678901234567890123
           4567890123456789012345678
          901234567890123456789012345
         67890123456789012345678901234
        5678901234567890123456789012345
       678901234567890123456789012345678
      90123456789012345678901234567890123
     4567890123456789012345678901234567890
    123456789012345678901234567890123456789
    '''
    # Insert your code here
    # one method
    count = 0
    for i in range(height):
        print(' ' * (height - i - 1), end='')
        for j in range(2 * i + 1):
            print(count % 10, end='')
            count += 1
        print()
    # another method
    count = 0
    lines = []
    for i in range(height):
        line = []
        for j in range(2 * i + 1):
            line.append(str(count % 10))
            count += 1
        lines.append(line)
    for i in range(height):
        print(' ' * (height - i - 1), end='')
        print(''.join(lines[i]))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
