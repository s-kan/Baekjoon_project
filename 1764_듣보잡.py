n, m = map(int, input().split())
listen = []
see = []
result = []
for i in range(n):
    listen.append(input())
for i in range(m):
    see.append(input())
listen = set(listen)
see.sort()
for i in see:
    if i in listen:
        result.append(i)
print(len(result))
for i in result:
    print(i)
