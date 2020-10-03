import sys

try:
    hero_powers = [int(x) for x in input("Please input the heroes' powers: ").split()]
    if any(i != int(i) for i in hero_powers):
        raise ValueError
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()
try:
    nb_of_switches = int(input('Please input the number of power flips: '))
    if nb_of_switches < 0 or nb_of_switches > len(hero_powers):
        raise ValueError
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()
# modify the try except functions from quiz3

first = sorted(hero_powers.copy())
i = 0
while i <= nb_of_switches - 1:
    first[0] = -first[0]
    first.sort()
    i += 1
sum1 = sum(first)
print(f'Possibly flipping the power of the same hero many times, the greatest achievable power is {sum1}.')
# use sort to find the smallest number and change the value and sort it again until times use out

second = sorted(hero_powers.copy())
j = 0
while j <= nb_of_switches - 1:
    second[j] = -second[j]
    j += 1
sum2 = sum(second)
print(f'Flipping the power of the same hero at most once, the greatest achievable power is {sum2}.')
# use sort to find the smallest number and change the value from smallest to largest depend on the times

third = hero_powers.copy()
select = []
if nb_of_switches < len(third):
    n = 0
    while n <= (len(third) - nb_of_switches + 1) - 1:
        sum_select = sum(third[n:n + nb_of_switches])
        select.append(sum_select)
        n += 1
    min_select = min(select)
    sum3 = sum(third) - 2 * min_select
    print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {sum3}.')
if nb_of_switches == len(third):
    sum3 = -sum(third)
    print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {sum3}.')
# traverses the loop with nb_of_switches length and find the smallest sum and minus twice its value

forth = hero_powers.copy()
group, final_select = [], []
m = 0
while m <= len(forth) - 1:
    group.append(forth[m])
    sum_group = -sum(group)
    if sum_group <= 0:
        group = []
    else:
        final_select.append(sum_group)
    m += 1
if len(final_select) != 0:
    max_select = max(final_select)
    sum4 = sum(forth) + 2 * max_select
else:
    sum4 = sum(forth)
print(f'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {sum4}.')
# find all the possible group and sum its value, if -sum >0,this group is useless, find the max and plus twice
