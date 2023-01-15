s = list(input())
a = 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        a += 1
ans = a//2
print(ans)