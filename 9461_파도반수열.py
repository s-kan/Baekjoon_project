import sys

t = int(sys.stdin.readline())
arr = [1,1,1,2,2,3,4,5,7,9]
for i in range(t):
    n = int(sys.stdin.readline())-1
    if n < 10:
        print(arr[n])
    else:
        for j in range(n-9):
            arr.append(arr[-1]+arr[-5])
        print(arr[n])