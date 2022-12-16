a, b, c = map(int, input().split())
d = int(input())

a1 = d//3600
b1 = (d-a1*3600)//60
c1 = d - 3600*a1 - 60*b1

a2 = a+a1
b2 = b+b1
c2 = c+c1

gqp = 0
if c2 >= 60:
    gqp = c2//60
    c2 = c2%60

b2 += gqp
gqp = 0
if b2 >= 60:
    gqp = b2//60
    b2 = b2%60

a2 += gqp
gqp = 0
if a2 >= 24:
    a2 = a2%24
print(a2, b2, c2)