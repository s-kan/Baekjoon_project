import sys
import math

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    n_2 = n*2
    arr = [True for _ in range(n_2 + 1)]
    for i in range(2, int(math.sqrt(n_2))+1):
        if arr[i]:
            j = 2
            while i*j <= n_2:
                arr[i*j] = False
                j += 1
    cnt = 0
    for i in range(n+1, n_2+1):
        if arr[i]:
            cnt += 1
    print(cnt)
