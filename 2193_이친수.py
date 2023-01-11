from math import *

n = int(input())
ans = 0

for i in range((n-1)//2+1):
    oi = i
    o = n-1-2*i
    ans += factorial(oi+o)//factorial(oi)//factorial(o)
print(ans)