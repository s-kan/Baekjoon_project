import sys
n, b = map(int, sys.stdin.readline().split())

ans = ''
while n > 0:
    tmp = n%b
    if tmp > 9:
        tmp = chr(tmp+55)
    else:
        tmp = str(tmp)
    ans = tmp + ans
    n = n//b
print(ans)
