import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())

def dfs(node):
    for i in graph[node]:
        if visited[i]:
            return
        visited[i] = True
        dfs(i)

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    visited = [False]*(n+1)
    graph = [[] for _ in range(n+1)]
    for j in range(n):
        graph[j+1].append(arr[j])
    cnt = 0
    for j in range(1, n+1):
        if not visited[j]:
            dfs(j)
            cnt += 1
    print(cnt)

