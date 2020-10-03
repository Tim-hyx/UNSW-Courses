# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.


# Insert your code here
def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print('The solutions are:')
print()
for a in range(10000, 99999):
    b = a + 2
    c = b + 4
    d = c + 6
    e = d + 8
    f = e + 10
    if isPrime(a) and isPrime(b) and isPrime(c) and isPrime(d) and isPrime(e) and isPrime(f):
        check_a_b = []
        for i in range(a + 1, b):
            if isPrime(i):
                check_a_b.append(i)
        check_b_c = []
        for i in range(b + 1, c):
            if isPrime(i):
                check_b_c.append(i)
        check_c_d = []
        for i in range(c + 1, d):
            if isPrime(i):
                check_c_d.append(i)
        check_d_e = []
        for i in range(d + 1, e):
            if isPrime(i):
                check_d_e.append(i)
        check_e_f = []
        for i in range(e + 1, f):
            if isPrime(i):
                check_e_f.append(i)
        if len(check_a_b) == 0 and len(check_b_c) == 0 and len(check_c_d) == 0 and len(check_d_e) == 0 and len(
                check_e_f) == 0:
            print(a, b, c, d, e, f)

