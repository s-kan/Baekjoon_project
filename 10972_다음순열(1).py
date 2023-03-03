import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(n-2, -1, -1):
    if arr[i]< arr[i+1]:
        for j in range(n-1, 0, -1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                arr = arr[:i+1] + sorted(arr[i+1:])
                print(' '.join(map(str, arr)))
                exit()
print(-1)