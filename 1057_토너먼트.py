import math

n, kim, im = map(int, input().split())
kim, im = sorted((kim, im))
cnt = 0
ans = -1
while n > 1:
    cnt += 1
    if kim%2 == 1 and kim+1 == im:
        ans = cnt
        break
    n = math.ceil(n/2)
    kim = math.ceil(kim/2)
    im = math.ceil(im/2)
print(ans)