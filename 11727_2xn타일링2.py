from math import *

n = int(input())
ans = 0
for i in range(n//2+1):
    a, b = i, n-2*i
    ans += factorial(a+b)//factorial(a)//factorial(b) * 2**a
print(ans%10007)