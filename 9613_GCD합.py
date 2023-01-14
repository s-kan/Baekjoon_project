import sys

def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)
t = int(sys.stdin.readline())
for i in range(t):
    arr = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for j in range(1, len(arr)-1):
        for k in range(j+1, len(arr)):
             ans += gcd(arr[j], arr[k])
    print(ans)
