n = int(input())

cnt = 0
if n < 100:
    cnt = n
elif 100 <= n <= 110:
    cnt = 99
else:
    cnt = 99
    for i in range(111, n+1):
        a = i//100
        b = i%100//10
        c = i%10
        if a-b == b-c:
            cnt += 1
print(cnt)