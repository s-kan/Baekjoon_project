n = int(input())
arr = []
for i in range(n):
    a = list(input().split())
    for j in range(1, len(a)):
        a[j] = int(a[j])
    arr.append(a)
arr.sort(key = lambda x:(-x[1], x[2], -x[3], x[0]))
for i in arr:
    print(i[0])