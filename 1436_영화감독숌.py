import sys
n = int(sys.stdin.readline())

num = 666
for i in range(n-1):
    while(1):
        num += 1
        s = str(num)
        if '666' in s:
            break

print(num)
