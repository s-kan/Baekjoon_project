import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
left = 0
right = 0
s = arr[0]
while left < n and right < n:
    if s < m:
        if right == n-1:
            break
        right += 1
        s += arr[right]
    else:
        if s == m:
            ans += 1
        if left == n-1:
            break
        if left == right:
            left += 1
            right += 1
            s = arr[left]
        else:
            s -= arr[left]
            left += 1

print(ans)