import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    cnt = 0
    visited = [False]*(n+1)
    for j in range(1, n+1):
        if not visited[j]:
            idx = j
            while not visited[idx]:
                visited[idx] = True
                idx = arr[idx]
            cnt += 1
    print(cnt)