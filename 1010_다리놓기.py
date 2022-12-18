from math import *

t = int(input())
for i in range(t):
    w, e = map(int, input().split())
    print(comb(e, w))