n = input()
arr = [0]*10

for i in n:
    arr[int(i)] += 1

result = max(arr)
mas = []
for i in range(len(arr)):
    if arr[i] == result:
        mas.append(i)
if (len(mas) == 1 and (mas[0] == 6 or mas[0] == 9)) or ((len(mas) == 2) and (mas[0] == 6 and mas[1] == 9)):
    result -= abs(arr[6]-arr[9])//2
print(result)
