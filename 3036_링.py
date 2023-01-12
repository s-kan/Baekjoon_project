n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

for i in range(1, n):
    g = gcd(arr[0], arr[i])
    print(arr[0]//g, end='')
    print('/', end='')
    print(arr[i]//g)