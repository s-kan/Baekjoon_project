arr = []
for i in range(8):
    arr.append(list(input()))
cnt = 0

for i in range(0, 8, 2):
    for j in range(0, 8, 2):
        if arr[i][j] == 'F':
            cnt += 1
for i in range(1, 8, 2):
    for j in range(1, 8, 2):
        if arr[i][j] == 'F':
            cnt += 1
print(cnt)
