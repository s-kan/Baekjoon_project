n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(k):
        ans = 0
        for x in range(m):
            ans += a[i][x]*b[x][j]
        print(ans, end=' ')
    print()
