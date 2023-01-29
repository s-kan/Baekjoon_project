import math

a, l = map(int, input().split())
max_val = a*l
min_val = a*(l-1)

for i in range(min_val, max_val+1):
    if math.ceil(i/a) == l:
        ans = i
        break
print(ans)