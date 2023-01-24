import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    d = {}
    m = int(input())
    for j in range(m):
        v, k = map(str, input().split())
        if k in d:
            d[k].append(v)
        else:
            d[k] = [v]
    ans = 0
    tmp = 1
    for j in d:
        tmp *= len(d[j])+1
    ans += tmp
    print(ans-1)