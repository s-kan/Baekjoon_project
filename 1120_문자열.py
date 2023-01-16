a, b = input().split()

tmp = len(b)-len(a)
anss = []
for i in range(tmp+1):
    b_tmp = b[i:i+len(a)]
    ans = 0
    for j in range(len(a)):
        if a[j] != b_tmp[j]:
            ans += 1
    anss.append(ans)
print(min(anss))