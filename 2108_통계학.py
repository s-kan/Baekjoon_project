import sys

n = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline()) for _ in range(n)])
mode_dic = {}
mode_arr = []

for i in arr:
    if i in mode_dic:
        mode_dic[i] += 1
    else:
        mode_dic[i] =1
all_values = mode_dic.values()
max_mode = max(all_values)

for i in mode_dic:
    if mode_dic[i] == max_mode:
        mode_arr.append(i)
print(round(sum(arr)/n))
print(arr[(n-1)//2])
if len(mode_arr) == 1:
    print(mode_arr[0])
else:
    print(mode_arr[1])
print(arr[-1]-arr[0])
