import math

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0
for i in arr:
    tmp = i
    ans += 1
    tmp -= b
    if tmp < 1:
        continue
    ans += math.ceil(tmp/c)
print(ans)

