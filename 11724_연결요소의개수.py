import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False]*(n+1)
visited[0] = True
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def dfs(node):
    for i in graph[node]:
        if visited[i]:
            continue
        visited[i] = True
        dfs(i)
for j in range(1, n+1):
    if not visited[j]:
        visited[j] = True
        dfs(j)
        cnt += 1
print(cnt)