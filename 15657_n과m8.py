n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(n):
        if len(s) == 0:
            s.append(arr[i])
        elif s[-1] <= arr[i]:
            s.append(arr[i])
        else:
            continue
        dfs()
        s.pop()
dfs()