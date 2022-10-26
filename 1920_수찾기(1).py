import sys

n = int(sys.stdin.readline())
arr = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr_t = map(int, sys.stdin.readline().split())

def Binary_s(t, arr, start, end):
    if start>end:
        return 0
    m = (start+end)//2
    if t == arr[m]:
        return 1
    elif t < arr[m]:
        return Binary_s(t, arr, start, m-1)
    else:
        return Binary_s(t, arr, m+1, end)

for i in arr_t:
    start = 0
    end = len(arr)-1
    print(Binary_s(i, arr, start, end))