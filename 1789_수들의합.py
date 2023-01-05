n = int(input())
idx = 1
s = 0
ans = 0
while True:
    if s+idx > n:
        if n-s > idx:
            ans += 1
        break
    s += idx
    idx += 1
    ans += 1
print(ans)