from math import *

n = int(input())

def comb(n, k):
    return factorial(n)//factorial(n-k)//factorial(k)

result = 1
for i in range(n//2):
    result += comb(n-(i+1), i+1)

print(result%10007)