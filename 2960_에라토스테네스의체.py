n, k = map(int, input().split())
arr = [i for i in range(2, n+1)]
cnt = 0
idx = 0
tmp = 2
while True:
    if arr[idx] != 0:
        if cnt == k-1:
            print(arr[idx])
            break
        arr[idx] = 0
        idx += tmp
        cnt += 1
    else:
        idx += tmp
    if idx > n-2:
        for i in range(len(arr)):
            if arr[i] != 0:
                idx = i
                tmp = arr[i]
                break

