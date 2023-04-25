import heapq, sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -tmp)