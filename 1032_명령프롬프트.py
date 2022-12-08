n = int(input())
str_arr = []

for i in range(n):
    str_arr.append(input())

result = str_arr[0]
if n != 1:
    for i in range(1, len(str_arr)):
        for j in range(len(result)):
            if result[j] == str_arr[i][j]:
                continue
            else:
                result = result[:j] + '?' + result[j+1:]

print(result)