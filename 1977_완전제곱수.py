m = int(input())
n = int(input())
sqr_nums = set([i**2 for i in range(1, 101)])
ans = []
for i in range(m, n+1):
    if i in sqr_nums:
        ans.append(i)
if len(ans) > 0:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)