import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(n):
    k, v = sys.stdin.readline().split()
    dic[k] = v
for _ in range(m):
    s = sys.stdin.readline().rstrip()
    print(dic[s])

