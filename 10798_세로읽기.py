arr = []
l_max = 0
for i in range(5):
    tmp = list(input())
    arr.append(tmp)
    if len(tmp) > l_max:
        l_max = len(tmp)
for i in range(5):
    arr[i] += [-1]*(l_max-len(arr[i]))

for i in range(l_max):
    for j in range(5):
        if arr[j][i] != -1:
            print(arr[j][i], end='')