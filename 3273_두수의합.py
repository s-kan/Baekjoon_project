n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr_1 = [0]*1000001
for i in arr:
    arr_1[i] = 1
ans = 0
for i in arr:
    tmp = x-i
    if i > x or tmp > 1000000:
        continue
    if arr_1[tmp] == 1:
        ans += 1
print(ans//2)