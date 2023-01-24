n = int(input())
s = []
visited = [False]*(n+1)

def dfs():
    if len(s) == n:
        print(' '.join(map(str, s)))
    for i in range(1, n+1):
        if visited[i]:
            continue
        s.append(i)
        visited[i] = True
        dfs()
        s.pop()
        visited[i] = False
dfs()