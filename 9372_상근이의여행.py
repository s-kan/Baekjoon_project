t = int(input())

def dfs(v):
    global cnt
    if s == n:
        cnts.append(cnt)
        return
    for i in range(n+1):
        if visited[i]:
            continue
        if graph[v][i] == 0:
            continue
        cnt += 1
        s += 1
        dfs(i)
        visited[v] = False

for i in range(t):
    n, m = map(int, input().split())
    graph = [[0]*(n+1) for _ in range(n+1)]
    print(graph)
    for j in range(m):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1
    for j in range(n+1):
        visited = [False] * (n + 1)
        visited[j] = True
        s = 0
        cnts = []
        cnt = 0
        dfs(j)

    print(min(cnts))