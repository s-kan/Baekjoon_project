x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()
if x[0] != x[1]:
    rx = x[0]
else:
    rx = x[2]

if y[0] != y[1]:
    ry = y[0]
else:
    ry = y[2]

print(rx, ry)

