k, n = map(int, input().split())
k_arr = [int(input()) for _ in range(k)]
start, end = 1, max(k_arr)

while start <= end:
    mid = (start+end)//2
    lan_num = 0
    for i in k_arr:
        lan_num += i//mid
    if lan_num >= n:
        start = mid+1
    else:
        end = mid-1
print(end)