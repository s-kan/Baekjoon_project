import sys

n = int(sys.stdin.readline())
distances = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

left = 0
right = 1
ans = prices[left]*distances[left]
while right<n-1:
    if prices[left] < prices[right]:
        ans += prices[left]*distances[right]
        right += 1
    else:
        ans += prices[right]*distances[right]
        left = right
        right = left + 1

print(ans)