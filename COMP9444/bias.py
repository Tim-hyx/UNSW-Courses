string = input('input string: ').replace(' ', '')
b, c, d, s = {}, 0, {}, {}
s[0] = string[string.find(')') + 1]
s[1] = '∧' if s[0] == '∨' else '∨'
a = string.split(s[0])
d[c] = [-1 if i[0] == '¬' else 1 for i in a]
b[c] = d[c].count(-1) - 0.5 - (len(d[c]) - 1) * s[0].count('∧')
print(f'l{c}: {d[c]}, b{c}: {b[c]}')
c += 1
for i in a:
    j = i[i.find('(') + 1:-1].split(s[1])
    d[c] = [-1 if k[0] == '¬' else 1 for k in j]
    b[c] = d[c].count(-1) - 0.5 - (len(d[c]) - 1) * s[1].count('∧')
    print(f'l{c}: {d[c]}, b{c}: {b[c]}')
    c += 1
print(b)
