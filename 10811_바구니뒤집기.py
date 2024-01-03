import sys

n, m = map(int, sys.stdin.readline().split())

arr = [i for i in range(1, n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    tmp = arr[a-1:b]
    idx = 0
    for j in range(a-1, b):
        arr[j] = tmp[len(tmp) - 1 - idx]
        idx += 1

print(' '.join(map(str, arr)))