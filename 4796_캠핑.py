idx = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    ans = 0
    tmp = v//p
    ans += tmp*l
    remain = v%p
    if remain > l:
        ans += l
    else:
        ans += remain
    print('Case', idx, end='')
    print(':', ans)
    idx += 1