import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    circles = []
    for j in range(n):
        circles.append(list(map(int, input().split())))
    ans = 0
    for j in circles:
        d1 = ((j[0]-x1)**2 + (j[1]-y1)**2)**0.5
        d2 = ((j[0]-x2)**2 + (j[1]-y2)**2)**0.5
        if d1 < j[2] and d2 > j[2]:
            ans += 1
        if d1 > j[2] and d2 < j[2]:
            ans += 1
    print(ans)