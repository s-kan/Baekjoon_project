def bin_serch(start, end, arr, x):
    if start>end:
        return 0
    m = (start+end)//2
    if arr[m]<x:
        return bin_serch(m+1, end, arr, x)
    elif arr[m]>x:
        return bin_serch(start, m-1, arr, x)
    else:
        return 1

n = int(input())
n_arr = sorted(list(map(int, input().split())))
m = int(input())
m_arr = list(map(int, input().split()))

for i in m_arr:
    print(bin_serch(0, n-1, n_arr, i), end=' ')