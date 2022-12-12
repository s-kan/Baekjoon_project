n = int(input())
arr = ['*' for i in range(n)]

for i in range(n):
    for j in range(n):
        print(arr[j], end='')
    print()
    arr[i] = ' '
