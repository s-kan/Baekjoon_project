import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


if arr == sorted(arr, key = lambda x : -x):
    print(-1)
else:
    for i in range(n-1, 0, -1):
        if arr[i] > arr[i-1]:
            if i == n-1:
                arr[i-1], arr[i] = arr[i], arr[i-1]
            else:
                tmp_arr = arr[i+1:]
                m_value = min(tmp_arr)
                if m_value > arr[i-1]:
                    idx = arr.index(m_value)
                    arr[i-1], arr[idx] = arr[idx], arr[i-1]
                    arr[i:] = sorted(arr[i:])
                else:
                    tmp_arr = sorted(arr[i:])
                    for j in tmp_arr:
                        if j > arr[i-1]:
                            tmp = j
                            break
                    idx = arr.index(tmp)
                    arr[i-1], arr[idx] = arr[idx], arr[i-1]
                    arr[i:] = sorted(arr[i:])
            break
    print(' '.join(map(str, arr)))