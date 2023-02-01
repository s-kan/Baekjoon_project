import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
sixs = []
ones = []
for _ in range(m):
    six, one = map(int, input().split())
    sixs.append(six)
    ones.append(one)
ans = []
six_min = min(sixs)
one_min = min(ones)
repeat = n//6
for i in range(repeat+1):
    ans.append(i*six_min + (n-6*i)*one_min)
ans.append(math.ceil(n/6)*six_min)
print(min(ans))
