n, m, v = map(int, input().split())
arr = []

for i in range(n+1):
    arr.append([0]*(n+1))
for i in range(m):
    a, b = map(int, input().split())
    arr[a][b]= arr[b][a]= 1

visited1 = [False]*(n+1)
ans1 = [v]
visited1[v] = True
def dfs(start):
    for i in range(1, n+1):
        if visited1[i]:
            continue
        elif arr[start][i] == 1:
            ans1.append(i)
            visited1[i] = True
            dfs(i)

visited2 = [False]*(n+1)
ans2 = [v]
visited2[v] = True

def bfs(start):
    queue = [start]
    while queue:
        idx = 0
        for nx in arr[queue.pop()]:
            if idx == n+1:
                break
            if (not visited2[idx]) and nx == 1:
                visited2[idx] = True
                queue.insert(0, idx)
                ans2.append(idx)
            idx += 1


dfs(v)
bfs(v)
print(' '.join(map(str, ans1)))
print(' '.join(map(str, ans2)))

