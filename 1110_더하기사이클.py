n = int(input())
if n < 10:
    n *= 10

def cycle(num):
    n1 = num%10
    n2 = num//10
    a = (n1 + n2)%10
    b = n1
    return b*10 + a

result = 1
c_n = cycle(n)
while c_n != n:
    result += 1
    c_n = cycle(c_n)

print(result)