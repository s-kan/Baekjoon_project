n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
visited = [False]*(arr[-1]+1)
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in arr:
        if visited[i]:
            continue
        s.append(i)
        visited[i] = True
        dfs()
        s.pop()
        visited[i] = False
dfs()