from collections import deque

n = int(input())
p = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(p):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
def bfs(v):
    visited[v] = 1
    queue = [v]
    while queue:
        for nx in graph[queue.pop()]:
            if visited[nx] == 0:
                visited[nx] = 1
                queue.insert(0, nx)
bfs(1)
print(sum(visited)-1)