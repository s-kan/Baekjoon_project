import sys

input = sys.stdin.readline

# def dfs():
#     if arr[i-1][j-1] != 1 and


while(1):
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    cnt = 0
    arr = []
    for i in range(h):
       tmp = list(map(int, input().split()))
       arr.append(tmp)
    i = j = 0
    while(1):
        if arr[i][j] == 1:
            dfs()
    print(arr)
    print(visited)