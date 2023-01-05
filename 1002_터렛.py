t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis_jb = ((x2-x1)**2 + (y2-y1)**2)**0.5
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if dis_jb < abs(r1-r2):
            print(0)
        elif dis_jb == abs(r1-r2):
            print(1)
        elif abs(r1-r2) < dis_jb < r1+r2:
            print(2)
        elif dis_jb == r1+r2:
            print(1)
        else:
            print(0)
