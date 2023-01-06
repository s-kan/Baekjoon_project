na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
amb = a-b
bma = b-a
ans = amb | bma
print(len(ans))
