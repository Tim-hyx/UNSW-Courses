# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers, i < j < k,
# every digit occurs at most once in i, j and k,
# and the product of i, j and k is a 6-digit number
# consisting precisely of the digits that occur in i, j and k.


# Insert your code here
for i in range(10, 97):
    for j in range(i + 1, 98):
        for k in range(j + 1, 99):
            number = ''
            number += str(i)
            number += str(j)
            number += str(k)
            check = set()
            for n in number:
                check.add(n)
            product = i * j * k
            num = []
            for m in str(product):
                num.append(m)
            num = set(num)
            if len(check) == 6 and len(str(product)) == 6 and len(num) == 6 and num == check:
                print(f'{i} x {j} x {k} = {product} is a solution.')

