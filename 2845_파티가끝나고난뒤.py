l, p = map(int, input().split())
arr = list(map(int, input().split()))
v = l*p
result = []
for i in arr:
    result.append(i-v)
for i in result:
    print(i, end=' ')