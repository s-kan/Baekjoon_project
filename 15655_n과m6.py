n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(len(arr)):
        if len(s) == 0:
            s.append(arr[i])
        elif arr[i]>s[-1]:
            s.append(arr[i])
        else:
            continue
        dfs()
        s.pop()
dfs()