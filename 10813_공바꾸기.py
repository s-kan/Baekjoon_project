import sys
input = sys.stdin.readline

n, m = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    tmp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = tmp

print(' '.join(map(str, arr)))
