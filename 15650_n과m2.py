n, m = map(int, input().split())

visited = [False]*9
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n+1):
        if i in visited:
            continue
        s.append(i)
        visited[i] = True
        dfs(i+1)
        s.pop()
        visited[i] = False
dfs(1)