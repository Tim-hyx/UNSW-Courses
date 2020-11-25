from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
import sys

# Insert your code here
a = input('Input a seed for the random number generator: ')
seed(int(a))
b = input('How many elements do you want to generate? ')
print()
list = []
for i in range(int(b)):
    c = randint(-50, 50)
    list.append(c)
print('The list is:', list)
print()
sum_number = sum(list)
mean = sum_number / int(b)
print('The mean is ', '%.2f' % (mean), '.', sep='')
list.sort()
if int(b) == 1:
    median = list[0]
elif int(b) % 2 == 1:
    median = list[int((int(b) - 1) / 2)]
else:
    median = (list[int(int(b) / 2)] + list[int(int(b) / 2 - 1)]) / 2
print('The median is ', '%.2f' % (median), '.', sep='')
sum_num = 0
for j in list:
    sum_num += (j - mean) * (j - mean)
standaer_dviation = sqrt(sum_num / int(b))
print('The standard deviation is ', '%.2f' % (standaer_dviation), '.', sep='')
print()
print('Confirming with functions from the statistics module:')
print('The mean is ', '%.2f' % (mean), '.', sep='')
print('The median is ', '%.2f' % (median), '.', sep='')
print('The standard deviation is ', '%.2f' % (standaer_dviation), '.', sep='')
