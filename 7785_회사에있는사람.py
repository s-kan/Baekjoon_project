import sys

n = int(sys.stdin.readline())
d = {}
for _ in range(n):
    name, state = map(str, sys.stdin.readline().split())
    if state == 'enter':
        d[name] = 1
    else:
        d[name] = 0
ans = []
for i in d:
    if d[i] == 1:
        ans.append(i)
ans.sort(reverse = True)
for i in ans:
    print(i)