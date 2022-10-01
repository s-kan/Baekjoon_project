import sys

N = list(map(int, sys.stdin.readline().split()))

b = max(N)
s = min(N)
r = b%s

while(r != 0):
    tmp = s
    s = r
    r = tmp%r
print(s)
print(int(N[0]*N[1]/s))