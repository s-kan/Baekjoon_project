import sys
n = int(sys.stdin.readline())

arr = list(range(1, n+1))

while len(arr) > 1:
    if len(arr) % 2:
        t = [arr[-1]]
        t.extend(arr[1::2])
        arr = t
    else:
        arr = arr[1::2]

print(arr[0])