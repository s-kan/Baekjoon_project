import sys

n = int(sys.stdin.readline())
arr = [0]*10001

for i in range(n):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)