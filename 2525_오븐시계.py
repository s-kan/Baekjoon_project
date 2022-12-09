a, b = map(int, input().split())
time = int(input())

if b+time >= 60:
    a += (time+b)//60
    b = (b+time)%60
else:
    b += time

if a >= 24:
    a = a-24

print(a, b)