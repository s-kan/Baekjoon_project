import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input().rstrip())
ans = 0
for _ in range(m):
    tmp = input().rstrip()
    if tmp in s:
        ans += 1
print(ans)