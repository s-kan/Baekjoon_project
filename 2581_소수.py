m = int(input())
n = int(input())
def isPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for j in range(2, x//2+2):
        if x%j == 0:
            return False
    return True

arr = []
for i in range(m, n+1):
    if isPrime(i):
        arr.append(i)
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])


