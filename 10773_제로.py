import sys
n = int(sys.stdin.readline())

arr = [0]*n
for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        arr.append(num)
    else:
        arr.pop()

sum = 0
if len(arr) == 0:
    print(0)
else:
    for i in range(len(arr)):
        sum += arr[i]
print(sum)