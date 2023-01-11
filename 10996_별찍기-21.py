import math

n = int(input())

for i in range(n):
    print(' '.join('*'*(math.ceil(n/2))))
    print('', ' '.join('*'*(n//2)))