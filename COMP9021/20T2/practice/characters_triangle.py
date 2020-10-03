# Prompts the user for a strictly positive number N
# and outputs an equilateral triangle of height N.
# The top of the triangle (line 1) is labeled with the letter A.
# For all nonzero p < N, line p+1 of the triangle is labeled
# with letters that go up in alphabetical order modulo 26
# from the beginning of the line to the middle of the line,
# starting wth the letter that comes next in alphabetical order
# modulo 26 to the letter in the middle of line p,
# and then down in alphabetical order modulo 26
# from the middle of the line to the end of the line.


# Insert your code here
height = int(input('Enter a strictly positive integer: '))
start = ord('A')
for i in range(1, height + 1):
    print(' ' * (height - i), end='')
    line = ''
    for j in range(i):
        line += chr(start + (int(i * (i - 1) / 2) + j) % 26)
    print(line + line[-2::-1])

