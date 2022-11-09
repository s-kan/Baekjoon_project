n = int(input())

str = []
arr = []
stack_arr = []
for i in range(n):
    arr.append(int(input()))

index = 0
for i in range(1, n+1):
    stack_arr.append(i)
    str.append('+')
    while(1):
        if len(stack_arr) == 0:
            break
        if stack_arr[-1] == arr[index]:
            stack_arr.pop()
            str.append('-')
            index+=1
        else:
            break

if len(stack_arr) > 0:
    print('NO')
else:
    for i in range(len(str)):
        print(str[i])