num = 8

for n in range(num - 1):
    print((num - n) * ' ' + (2*n+1) * '*')

for n in range(num - 1, -1, -1):
    print((num - n) * ' ' + (2*n+1) * '0')