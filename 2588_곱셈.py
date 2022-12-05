a = int(input())
b = int(input())

n1 = b%10
n2 = b%100//10
n3 = b//100

print(a*n1)
print(a*n2)
print(a*n3)
print(a*n1+a*n2*10+a*n3*100)