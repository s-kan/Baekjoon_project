arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort()
v = sum(arr) - 100

for i in range(8):
    for j in range(i+1, 9):
        if arr[i]+arr[j] == v:
            a, b = arr[i], arr[j]
            arr.remove(a)
            arr.remove(b)
            break
    if len(arr) == 7:
        break

for i in arr:
    print(i)