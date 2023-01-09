n = int(input())
ans = 0
arr = [[0 for _ in range(100)] for _ in range(100)]
for i in range(n):
    a, b = map(int, input().split())
    for j in range(b-1, b+9):
        arr[j][a-1:a+9] = [1]*10

cnt = 0
for i in arr:
    cnt += i.count(0)
print(10000-cnt)