import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(n):
    s = 0
    for j in range(i, n):
        s += arr[j]
        if s == m:
            ans += 1
            break
        elif s > m:
            break
print(ans)