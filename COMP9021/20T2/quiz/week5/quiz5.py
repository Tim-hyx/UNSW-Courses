# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Uses National Data on the relative frequency of given names in the
# population of U.S. births, stored in a directory "names", in files
# named "yobxxxx.txt with xxxx (the year of birth)
# ranging from 1880 to 2018.
# The "names" directory is a subdirectory if the working directory.
# Prompts the user for a male first name, and finds out the years
# when this name was most popular in terms of ranking amongst male names.
# Displays the ranking, and the years in decreasing order of frequency,
# computed, for a given year, as the count of the name for the year
# divided by the sum of the counts of all male names for the year.


import csv
from pathlib import Path
from collections import defaultdict
import sys

cwd = Path.cwd()
possible_path_1 = cwd.parent.parent / 'names'
possible_path_2 = Path(cwd.root) / 'course' / 'data' / 'names'
if possible_path_1.exists():
    # FOR ME
    path = possible_path_1
elif possible_path_2.exists():
    # FOR ED
    path = possible_path_2
else:
    # FOR YOU, names IS A SUBDIRECTORY OF THE WORKING DIRECTORY
    path = Path('names')

# INSERT YOUR CODE HERE
try:  # use the idea from assignment and quiz try except function
    first_name, ranking, year = input('Enter a male first name: '), defaultdict(list), 1880
    while year <= 2018:
        if Path.exists(path / f'yob{year}.txt'):
            with open(path / f'yob{year}.txt') as file:
                names = []
                times = []
                for lines in file:
                    name, gender, time = lines.split(',')  # an example: Roscoe,M,102
                    if gender == 'M':
                        times.append(time)
                        names.append(name)
                if first_name in names:  # make sure the name in the list
                    times = [int(time) for time in times]
                    given_year = times[names.index(first_name)] / sum(
                        times)  # find the index of the first name and use divided
                    ranking[names.index(first_name)].append((given_year, year))
        year += 1
    if len(ranking) == 0:
        raise ValueError
    else:
        # displays the ranking, and the years in decreasing order of frequency
        ranking[min(ranking.keys())].sort(reverse=True)
        rank, years, i, j = ranking[min(ranking.keys())], [], 0, 0
        while i <= len(rank) - 1:
            years.append(str(rank[i][1]))  # rank includes a tuple (given_year, year),so need the year
            i += 1
        print(f'By decreasing order of frequency, {first_name} was most popular in the following years:')
        while j <= len(years) - 1:
            print('    ' + ' '.join(years[j:j + 5]))  # output every 5 years
            j += 5
        print(f'Its rank was {min(ranking.keys()) + 1} then.')
except ValueError:
    print(f'{first_name} is not a male first name in my records.')
    sys.exit()
