import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    arr = []
    for j in range(n+2):
        arr.append([0]*(m+2))
    for j in range(k):
        x, y = map(int, input().split())
        arr[y+1][x+1] = 1
    ans = 0
    def dfs(start, end):
        arr[start][end] = 0
        if arr[start][end - 1] == 0 and arr[start][end + 1] == 0 and arr[start + 1][end] == 0 and arr[start-1][end] == 0:
            return
        if arr[start][end - 1] == 1:
            dfs(start, end - 1)
        if arr[start + 1][end] == 1:
            dfs(start + 1, end)
        if arr[start][end + 1] == 1:
            dfs(start, end + 1)
        if arr[start-1][end] == 1:
            dfs(start-1, end)
    for j in range(n+1):
        for k in range(m+1):
            if arr[j][k] == 1:
                dfs(j, k)
                ans += 1
    print(ans)


