N = int(input())
b = 0

for i in range(N):
    a = i
    r = 0
    while(a>0):
        r = r+a%10
        a = int(a/10)
    if (i+r) == N:
        b = i
        break
    else:
        continue

print(b)