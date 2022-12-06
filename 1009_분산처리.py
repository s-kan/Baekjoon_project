n = int(input())
r = []
for i in range(n):
    a, b = map(int, input().split())
    arr = [a%10]
    while True:
        if arr[-1]*a%10 == arr[0]:
            break
        else:
            arr.append(arr[-1]*a%10)
    if arr[b%len(arr)-1] == 0:
        r.append(10)
    else:
        r.append(arr[b%len(arr)-1])
for i in r:
    print(i)