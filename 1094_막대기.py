x = int(input())

for i in range(6, -1, -1):
    if 2**i <= x:
        n = i
        break
ans = 0
for i in range(n, -1, -1):
    tmp = x//2**i
    x = x%2**i
    ans += tmp
print(ans)