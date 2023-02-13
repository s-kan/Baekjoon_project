n = int(input())
arr = list(map(int, input().split()))
dp = []
dp.append(arr[0])
tmp = arr[0]
for i in range(1, n):
    tmp += arr[i]
    if arr[i] < tmp:
        dp.append(tmp)
    else:
        dp.append(arr[i])
        tmp = arr[i]
print(max(dp))