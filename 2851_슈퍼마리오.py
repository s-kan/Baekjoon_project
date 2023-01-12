arr = []
for i in range(10):
    arr.append(int(input()))
ans = 0
if sum(arr)<=100:
    ans = sum(arr)
else:
    for i in range(len(arr)):
        if ans+arr[i]>100:
            if 100-ans < ans+arr[i]-100:
                break
            else:
                ans += arr[i]
                break
        else:
            ans += arr[i]
print(ans)