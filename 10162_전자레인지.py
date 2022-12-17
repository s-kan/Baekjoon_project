t = int(input())
a = 300
b = 60
c = 10
ra = rb = rc = 0

if t%10 != 0:
    print(-1)
else:
    if t >= a:
        ra = t//a
        t = t%a
    if t >= b:
        rb = t//b
        t = t%b
    if t >= c:
        rc = t//c
        t = t%c
    print(ra, rb, rc)