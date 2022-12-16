n, k = map(int, input().split())
arr = [int(input()) for i in range(n)]

result = 0

for i in range(n-1, -1, -1):
    if k >= arr[i]:
        result += k//arr[i]
        k = k%arr[i]
    if k == 0:
        break

print(result)
