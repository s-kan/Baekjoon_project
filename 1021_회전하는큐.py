n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
p_arr = list(map(int, input().split()))
result = 0
cur = 1
for i in p_arr:
    if arr[0] == i:
        arr.remove(i)
    else:
        idx = arr.index(i)
        a = min(idx, len(arr)-idx)
        arr = arr[idx:] + arr[:idx]
        arr.remove(i)
        result += a
print(result)