import sys

input = sys.stdin.readline
t = int(input())

def dfs(node, cnt):
    visited[node] = True
    for j in graph[node]:
        if not visited[j]:
            cnt = dfs(j, cnt+1)
    return cnt
for i in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for j in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False]*(n+1)
    cnt = dfs(1, 0)
    print(cnt)
