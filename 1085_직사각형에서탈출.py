x, y, w, h = map(int, input().split())

b = []
b.append(x)
b.append(y)
b.append(w-x)
b.append(h-y)

print(min(b))