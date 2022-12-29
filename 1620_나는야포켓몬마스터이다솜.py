import sys

n, m = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]
d = {}
for i in range(n):
    d[arr[i]] = i+1
for i in range(m):
    tmp = sys.stdin.readline().rstrip()
    if 65 <= ord(tmp[0]) <= 90 or 97 <= ord(tmp[0]) <= 122:
        print(d[tmp])
    else:
        print(arr[int(tmp)-1])
