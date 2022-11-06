import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

rank = [1]*n
index = 0
for i in arr:
    for j in arr:
        if i[0]<j[0] and i[1]<j[1]:
            rank[index] += 1
    index += 1
for i in range(len(rank)):
    print(rank[i], end = ' ')