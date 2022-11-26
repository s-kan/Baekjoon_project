n, k = map(int, input().split())

arr = [i+1 for i in range(n)]
result = []
current = k-1
while(1):
    result.append(arr.pop(current))
    if len(arr)==0:
        break
    if current + k - 1 > len(arr) - 1:
        current = (current + k - 1)%len(arr)
    else:
        current += k - 1
    if current > len(arr)-1:
        current = 0

print('<', end='')
for i in range(n-1):
    print(result[i], end='')
    print(',', end=' ')
print(result[-1], end='')
print('>')