import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merge_arr = []
    l = h = 0
    while l < len(low_arr) and h <len(high_arr):
        if len(str(low_arr[l])) < len(str(high_arr[h])):
            merge_arr.append(low_arr[l])
            l += 1
        else:
            merge_arr.append(high_arr[h])
            h += 1
    merge_arr += low_arr[l:]
    merge_arr += high_arr[h:]
    return merge_arr

arr = merge_sort(arr)
r = []
for i in arr:
    if i not in r:
        r.append(i)

size = len(str(r[0]))
start = 0
for i in range(len(r)):
    if len(str(r[0])) == len(str(r[-1])):
        r.sort()
        break
    elif len(str(r[i])) == size:
        continue
    elif len(str(r[i])) != size:
        r[start:i] = sorted(r[start:i])
        start = i
        size = len(str(r[i]))
        if(size == len(str(r[-1]))):
            break
r[start:len(r)] = sorted(r[start:len(r)])

for i in r:
    print(i)


