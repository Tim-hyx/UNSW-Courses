'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv
from collections import defaultdict


def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    lines = []
    with open('cpiai.csv') as open_file:
        for line in open_file:
            if line.isspace() or line.startswith('Date'):
                continue
            else:
                lines.append(line.strip())
    months_inflations = defaultdict(list)
    for line in lines:
        date, index, inflation = line.split(',')
        year_num, month, day = date.split('-')
        if year_num == str(year):
            months_inflations[float(inflation)].append(months[int(month) - 1])
    if months_inflations:
        max_value = max(months_inflations.keys())
        following_months = months_inflations[max_value]
        print(f'In {year}, maximum inflation was: {max_value}')
        print(f"It was achieved in the following months: {', '.join(following_months)}")


if __name__ == '__main__':
    import doctest

    doctest.testmod()
