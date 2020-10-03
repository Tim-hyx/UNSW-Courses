# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


from math import sqrt
from itertools import permutations


# A number is a good prime if it is prime and consists of nothing but
# distinct nonzero digits.
# Returns True or False depending on whether the integer provided as
# argument is or is not a good prime, respectively.
# Will be tested with for number a positive integer at most equal to
# 10_000_000.
def is_good_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    a=str(number)
    list=[]
    for i in a:
        list.append(i)
    for j in list:
        if j =='0':
            return False
        time=list.count(j)
        if time>1:
            return False
    return True
        # REPLACE PASS ABOVE WITH YOUR CODE

# pattern is expected to be a nonempty string consisting of underscores
# and digits of length at most 7.
# Underscores have to be replaced by digits so that the resulting number
# is the smallest good prime, in case it exists.
# The function returns that number if it exists, None otherwise.
def smallest_good_prime(pattern):
    if '_' not in pattern:
        number = int(pattern)
        if is_good_prime(number) and len(pattern) < 8:
            return pattern
    a=set(list('123456789'))
    b=set(pattern.replace('_',''))
    leftnumber=list(sorted(a-b))
    c=pattern.count('_')
    randomnumber=permutations(leftnumber,c)
    for i in randomnumber:
        patternlist=list(pattern)
        index=0
        for j in range(len(patternlist)):
            if patternlist[j]=='_':
                patternlist[j]=i[index]
                index=index+1
        num=int(''.join(patternlist))
        if is_good_prime(num):
            return num
    # REPLACE PASS ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS
