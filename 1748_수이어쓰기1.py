n = input()
l = len(n)
ans = 0
for i in range(1, len(n)):
    ans += i*(10**i - 10**(i-1))
ans += l*(int(n)-(10**(l-1)-1))
print(ans)