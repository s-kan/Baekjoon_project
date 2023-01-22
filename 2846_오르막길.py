n = int(input())
arr = list(map(int, input().split()))
a = [arr[0]]
ans = 0
for i in range(1, n):
    if arr[i-1] < arr[i]:
        a.append(arr[i])
        if i == n-1:
            tmp = a[-1]-a[0]
            if tmp > ans:
                ans = tmp
    else:
        if len(a) != 0:
            tmp = a[-1]-a[0]
            if tmp > ans:
                ans = tmp
            a = [arr[i]]
print(ans)

