a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

B = b1 * b2
A = a1 * b2 + a2 * b1

tmp = gcd(A, B)

print(A//tmp, B // tmp)