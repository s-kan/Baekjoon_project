import sys
import math

t = int(sys.stdin.readline())
arr = [i*(i+1)//2 for i in range(1, math.ceil(2000**0.5)+2)]
s = set()
for i in arr:
    for j in arr:
        for k in arr:
            s.add(i+j+k)
for i in range(t):
    n = int(sys.stdin.readline())
    if n in s:
        print(1)
    else:
        print(0)
