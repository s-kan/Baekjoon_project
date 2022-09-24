import sys
M, N = map(int, sys.stdin.readline().split())

def primenum(n):
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return 1
        else:
            continue
    return 0

for i in range(M, N+1):
    if primenum(i)==1 or i==1:
        continue
    else:
        print(i)

