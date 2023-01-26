import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()

left = 0
right = 0
cnt = 0
tmp = 0
value = 0
while True:
    if arr[left] == arr[right]:
        right += 1
        tmp += 1
    else:
        if tmp > cnt:
            value = arr[left]
            cnt = tmp
        left = right
        tmp = 0
    if right == n:
        if tmp > cnt:
            value = arr[left]
            cnt = tmp
        break
print(value)

