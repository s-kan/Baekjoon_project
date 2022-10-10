import sys

T = int(sys.stdin.readline())
t = []
for i in range(T*2):
    t.append(int(sys.stdin.readline()))

for i in range(0, T*2, 2):
    b = t[i]
    a = t[i+1]
    arr = [[0]*(a) for j in range(b+1)]
    for j in range(a):
        arr[0][j] = j+1
    for j in range(b):
        for k in range(a):
            if(k==0):
                arr[j+1][k] = 1
            else:
                arr[j+1][k] = arr[j+1][k-1] + arr[j][k]
    print(arr[b][a-1])

