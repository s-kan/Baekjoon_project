n = input()
arr = [0]*10

for i in n:
    if i == '6' or i == '9':
        arr[6] += 1
    else:
        arr[int(i)] += 1

if arr[6]%2 == 0:
    arr[6] = arr[6]//2
else:
    arr[6] = arr[6]//2+1
result = max(arr)
print(result)
