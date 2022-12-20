n, k = map(int, input().split())
arr = [i+1 for i in range(n)]
result = []
cur = 0
while arr:
    cur = (cur + k - 1)%len(arr)
    result.append(arr.pop(cur))

print("<", end='')
print(*result, sep=', ', end='')
print(">")