e, s, m = map(int, input().split())

if e == 15:
    e = 0
if s == 28:
    s = 0
if m == 19:
    m = 0

num = 1
while True:
    if num%15 == e and num%28 == s and num%19 == m:
        break
    else:
        num += 1
print(num)