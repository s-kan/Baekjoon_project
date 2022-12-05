n = int(input())
arr = [int(input()) for i in range(n)]

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    m = len(arr)//2
    low_arr = merge_sort(arr[:m])
    high_arr = merge_sort(arr[m:])
    l = h = 0
    a = []
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            a.append(low_arr[l])
            l += 1
        else:
            a.append(high_arr[h])
            h += 1
    a += low_arr[l:]
    a += high_arr[h:]
    return a

arr = merge_sort(arr)
for i in arr:
    print(i)