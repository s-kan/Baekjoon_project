arr = [int(input()) for _ in range(8)]
s_arr = sorted(arr)
ans = sum(s_arr[3:])
print(ans)
i_ans = []
for i in range(3, 8):
    i_ans.append(arr.index(s_arr[i])+1)
print(' '.join(map(str, sorted(i_ans))))