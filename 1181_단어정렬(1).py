import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())
s_l = set(arr)
lst=list(s_l)
lst.sort()
lst.sort(key = len)


for i in lst:
    print(i)