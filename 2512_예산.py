n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)
price = int(input())

if sum(arr) <= price:
    print(max(arr))
else:
    ans = max(arr)
    s = sum(arr)
    minus = 0
    while s > price:
        s += minus
        minus = 0
        for i in arr:
            if i > ans:
                minus += i-ans
            else:
                break
        s -= minus
        ans -= 1
    print(ans+1)