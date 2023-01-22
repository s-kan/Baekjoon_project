n = int(input())
arr = [[0, 0]]
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [0]*(n+1)
for i in range(1, n+1):
    tmp_arr = []
    for j in range(0, i):
        if j+arr[j+1][0] == i:
            tmp_arr.append(dp[j]+arr[j+1][1])
    d = 0
    if len(tmp_arr) != 0:
        d = max(tmp_arr)
    dp[i] = max(dp[i-1], d)

print(dp[-1])
