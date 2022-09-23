M, N = map(int, input().split())

A = []
for i in range(M):
    A.append(list(input()))
m = M-7
n = N-7

d = []

for i in range(m):
    for j in range(n):
        c = 0
        a = []
        for k in range(8):
            a.append(A[i+k][j:j+8])
        for x in range(0, 8, 2):
            for y in range(0, 8, 2):
                if a[x][y]=='B':
                    c = c+1
            for z in range(1, 8, 2):
                if a[x][z]=='W':
                    c = c+1
        for x in range(1, 8, 2):
            for y in range(0, 8, 2):
                if a[x][y]=='W':
                    c = c+1
            for z in range(1, 8, 2):
                if a[x][z]=='B':
                    c = c+1
        d.append(c)
        c = 0
        for x in range(0, 8, 2):
            for y in range(0, 8, 2):
                if a[x][y] == 'W':
                    c = c + 1
            for z in range(1, 8, 2):
                if a[x][z] == 'B':
                    c = c + 1
        for x in range(1, 8, 2):
            for y in range(0, 8, 2):
                if a[x][y] == 'B':
                    c = c + 1
            for z in range(1, 8, 2):
                if a[x][z] == 'W':
                    c = c + 1
        d.append(c)

print(min(d))