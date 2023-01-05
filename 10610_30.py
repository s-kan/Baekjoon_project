n = list(input())
n = list(map(int, n))

if sum(n)%3 != 0 or 0 not in n:
    print(-1)
else:
    n.sort(reverse=True)
    print(''.join(map(str, n)))
