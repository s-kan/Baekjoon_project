t = int(input())

arr = []
for i in range(t):
    a = int(input())
    if a == 0:
        print(1, 0)
    elif a == 1:
        print(0, 1)
    else:
        x0, x1 = 1, 0
        y0, y1 = 0, 1
        r0, r1 = 1, 1
        for i in range(a-2):
            x0, x1 = y0, y1
            y0, y1 = r0, r1
            r0, r1 = x0+y0, x1+y1
        print(r0, r1)
