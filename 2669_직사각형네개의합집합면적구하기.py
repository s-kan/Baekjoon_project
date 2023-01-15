arr = []
for i in range(102):
    arr.append([0]*101)

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        arr[j][x1:x2] = [1]*(x2-x1)

ans = 0
for i in arr:
    ans += sum(i)
print(ans)