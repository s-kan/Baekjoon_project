n = int(input())
arr = [[0, 0]]
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [0]*(n+1)
for i in range(2, n+1):
    tmp_arr = []
    for j in range(1, i+1):
        if j+arr[j][0]-1 == i:
            tmp_arr.append(dp[j]+arr[j][1])
    d = 0
    if len(tmp_arr) != 0:
        d = max(tmp_arr)
    dp[i] = max(dp[i-1], d)
print(arr)
print(dp)
print(dp[-1])
