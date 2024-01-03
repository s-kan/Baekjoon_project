import sys

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    l = r = k = 0

    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            arr[k] = left_arr[l]
            l += 1
        else:
            arr[k] = right_arr[r]
            r += 1
        k += 1
    if l == len(left_arr):
        while r < len(right_arr):
            arr[k] = right_arr[r]
            r += 1
            k += 1
    else:
        while l < len(left_arr):
            arr[k] = left_arr[l]
            l += 1
            k += 1
    return arr

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
none_rep = list(set(arr))
sorted_arr = merge_sort(none_rep)

ans_dict = {}
for i in range(len(sorted_arr)):
    ans_dict[sorted_arr[i]] = i

for i in range(len(arr)):
    print(ans_dict[arr[i]], end=' ')
