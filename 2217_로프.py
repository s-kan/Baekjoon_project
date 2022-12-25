n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr = sorted(arr, reverse=True)
result = []
for i in range(len(arr)):
    result.append((i+1)*arr[i])
print(max(result))