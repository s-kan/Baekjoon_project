import sys
input = sys.stdin.readline

def DFS(l, idx):
    global answer
    if l == n//2:
        a = b = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += arr[i][j]
                elif not visited[i] and not visited[j]:
                    b += arr[i][j]
        answer = min(answer, abs(a-b))
    for i in range(idx, n):
       if not visited[i]:
           visited[i] = True
           DFS(l+1, i)
           visited[i] = False


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
answer = int(1e9)

DFS(0, 0)
print(answer)