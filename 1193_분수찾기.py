n = int(input())

idx = 1
s = 0
while True:
    s += idx
    if s >= n:
        s -= idx
        break
    idx += 1

if idx%2 == 1:
    a = idx
    b = 1
    for i in range(s+1, n):
        a -= 1
        b += 1
else:
    a = 1
    b = idx
    for i in range(s+1, n):
        a += 1
        b -= 1

print('{0}/{1}'.format(a,b))