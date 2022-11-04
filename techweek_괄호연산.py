n = int(input())

arr=[]
for i in range(n):
    arr.append(list(input()))


for i in arr:
    s = [i[0]]
    s_index = 1
    for j in range(1, len(arr)):
        if i[j] == ')' and s[s_index] == '(':
            s[s_index] = 3
            if s[s_index] ==