n = int(input())
arr = list(map(int, input().split()))
price = int(input())
start, end = 1, max(arr)

while start <= end:
    mid = (start+end)//2

    tmp = 0
    for i in arr:
        if i > mid:
            tmp += i - mid
    s = sum(arr)-tmp

    if s > price:
        end = mid - 1
    else:
        start = mid + 1
print(end)