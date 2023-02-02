n = int(input())
arr = list(map(int, input().split()))
arr1 = []
tmp = 0
for i in range(n):
    arr1.append(sum(arr[:i]))
print(arr1)