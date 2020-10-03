# Prompts the user for a string w of lowercase letters and outputs the
# longest sequence of consecutive letters that occur in w,
# but with possibly other letters in between, starting as close
# as possible to the beginning of w.


import sys

# Insert your code here
word = input('Please input a string of lowercase letters: ')
d = {}
for x in word:
    if x in d:
        d[chr(ord(x) + 1)] = d[x] + x
    else:
        d[chr(ord(x) + 1)] = x
print(f'The solution is: {max(d.values(), key=len)}')

