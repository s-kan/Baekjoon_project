n = int(input())
arr = list(map(int, input().split()))
ans =  []

for i in range(n):
    tmp = []
    tmp.append(arr[i])
    for j in range(i, n):
        if arr[j] > tmp[-1]:
            tmp.append(arr[j])
    ans.append(len(tmp))

print(max(ans))
