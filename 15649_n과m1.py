n, m = map(int, input().split())

visited = [False]*9
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i] == True:
            continue
        s.append(i)
        visited[i] = True
        dfs()
        s.pop()
        visited[i] = False
dfs()