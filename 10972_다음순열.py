import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(n-1, 0, -1):
    if arr[i] > arr[i-1]:
        if i == n-1:
            tmp = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = tmp
            break
        else:
            tmp_arr = arr[i+1:]
            m_value = min(tmp_arr)
            if m_value > arr[i-1]:
                tmp = arr[i-1]
                arr[i-1] = m_value
                arr[tmp_arr.index(m_value)] = tmp
                arr[i:] = sorted(arr[i:])
                break
            else:
                tmp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = tmp
                arr[i:] = sorted(arr[i:])
                break
if arr == sorted(arr, key = lambda x : -x):
    print(-1)
else:
    print(' '.join(map(str, arr)))