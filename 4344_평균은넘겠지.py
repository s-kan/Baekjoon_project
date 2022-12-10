c = int(input())

for i in range(c):
    arr = list(map(int, input().split()))
    mean = sum(arr[1:])/arr[0]
    cnt = 0
    for j in range(1, len(arr)):
        if arr[j] > mean:
            cnt +=1
    print('{:.3f}%'.format(cnt/arr[0]*100))