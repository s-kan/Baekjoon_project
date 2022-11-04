import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr_s = list(sorted(set(arr)))

cnt = 0

for i in range(n):
    if arr[i] == arr_s[i]:
        continue
    else:
        temp = arr[i]
        j = arr.index(arr_s[i])
        arr[i] = arr_s[i]
        arr[j] = temp
        cnt += 1

print(cnt)