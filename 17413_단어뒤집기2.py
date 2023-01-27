arr = list(input())

tag = 0
for i in range(len(arr)):
    if arr[i] == '<':
        tag = 1
    elif arr[i] == '>':
        tag = 0
    elif tag == 0:
        if i == 0 or arr[i-1] == '>' or arr[i-1] == ' ':
            start = i
        if i == len(arr)-1:
            end = i+1
            tmp = arr[start:end]
            tmp.reverse()
            arr[start:end] = tmp
        elif arr[i+1] == '<' or arr[i+1] == ' ':
            end = i+1
            tmp = arr[start:end]
            tmp.reverse()
            arr[start:end] = tmp
print(''.join(map(str, arr)))
