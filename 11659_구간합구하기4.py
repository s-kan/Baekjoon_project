import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0]
tmp = 0
for i in arr:
    tmp += i
    prefix_sum.append(tmp)

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(prefix_sum[end]-prefix_sum[start-1])