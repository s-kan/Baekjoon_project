def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    l = h = k = 0
    while l<len(low_arr) and h<len(high_arr):
        if low_arr[l] < high_arr[h]:
            arr[k] = low_arr[l]
            l += 1
        else:
            arr[k] = high_arr[h]
            h += 1
        k += 1
    if l == len(low_arr):
        while h < len(high_arr):
            arr[k] = high_arr[h]
            h += 1
            k += 1
    elif h == len(high_arr):
        while l < len(low_arr):
            arr[k] = low_arr[l]
            l += 1
            k += 1
    return arr