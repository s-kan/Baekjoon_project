import heapq
import sys
input = sys.stdin.readline
arr = []
n = int(input())

for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, tmp)
