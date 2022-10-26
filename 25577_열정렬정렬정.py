import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr_s = sorted(arr)

count = 0
temp = 0

for i in range(N):
    if arr[i] == arr_s[i]:
        continue
    else:
        arr[i]