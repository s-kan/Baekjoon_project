n, m = map(int, input().split())

head = 1
for i in range(n, n-m, -1):
    head *= i
tail = 1
for i in range(1, m+1):
    tail *= i
print(head//tail)