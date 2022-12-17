t = int(input())
def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)


for i in range(t):
    A, B = map(int, input().split())
    g = gcd(A, B)
    print(A*B//g)