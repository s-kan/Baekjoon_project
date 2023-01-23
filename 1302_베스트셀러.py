import sys

n = int(sys.stdin.readline())
d = {}
for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    if tmp in d:
        d[tmp] += 1
    else:
        d[tmp] = 1
max_num = 0
for i in d:
    if d[i] > max_num:
        max_num = d[i]
ans_arr = []
for i in d:
    if d[i] == max_num:
        ans_arr.append(i)
ans_arr.sort()
print(ans_arr[0])
