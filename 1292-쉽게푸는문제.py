a, b = map(int, input().split())
n = 0
arr = []
tmp = 0
while n < b:
    tmp += 1
    n += tmp
    for i in range(tmp):
        arr.append(tmp)
result = 0
for i in range(a-1, b):
    result += arr[i]
print(result)