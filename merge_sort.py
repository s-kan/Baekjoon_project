def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    l = h = 0
    a = []
    while l<len(low_arr) and h<len(high_arr):
        if low_arr[l] < high_arr[h]:
            a.append(low_arr[l])
            l += 1
        else:
            a.append(high_arr[h])
            h += 1
    a += low_arr[l:]
    a += high_arr[h:]
    return a