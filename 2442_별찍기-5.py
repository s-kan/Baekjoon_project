n = int(input())

for i in range(1, n+1):
    s = '*'*(2*i-1)
    b = ' '*(n-i)
    print(b, end='')
    print(s)
