import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
ans.append(sum(arr[:k]))
l = 0
r = k-1
while r < n-1:
    tmp = ans[-1]
    tmp -= arr[l]
    r += 1
    l += 1
    tmp += arr[r]
    ans.append(tmp)
print(max(ans))