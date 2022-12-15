n = int(input())
arr = list(map(int, input().split()))
arr.sort()

s = 0
for i in arr:
    s += n*i
    n -= 1
print(s)