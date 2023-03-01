import sys

n = int(sys.stdin.readline())
arr = []
arr.append(['X']*(n+2))
for _ in range(n):
    tmp_arr = list(sys.stdin.readline().rstrip())
    tmp_arr = ['X'] + tmp_arr + ['X']
    arr.append(tmp_arr)
arr.append(['X']*(n+2))

for i in arr:
    print(*i)

ans = 0
for i in range(1, n+1):
    start = 1
    end = 1
    while end < n+1:
        if end == n:
            tmp = end - start + 1
            if ans < tmp:
                ans = tmp
            break
        else:
            if arr[i][start] == arr[i][end]:
                end += 1
            else:
                if arr[i][start] == arr[i-1][end] or arr[i][start] == arr[i][end] or arr[i][start] == arr[i][end+1]:
                    tmp = end - start + 1
                    end += 1
                    while arr[i][start] == arr[i][end] and end < n+1:
                        tmp += 1
                        end += 1
                    if ans < tmp:
                        ans = tmp
                    start = end
                else:
                    tmp = end - start
                    if ans < tmp:
                        ans = tmp
                    start = end

for j in range(1, n+1):
    start = 1
    end = 1
    while end < n+1:
        if end == n:
            tmp = end - start + 1
            if ans < tmp:
                ans = tmp
            break
        else:
            if arr[start][j] == arr[end][j]:
                end += 1
            else:
                if arr[start][j] == arr[end][j-1] or arr[start][j] == arr[end][j+1] or arr[start][j] == arr[end+1][j]:
                    tmp = end - start + 1
                    end += 1
                    while arr[start][j] == arr[end][j] and end < n+1:
                        tmp += 1
                        end += 1
                    if ans < tmp:
                        ans = tmp
                    start = end
                else:
                    tmp = end - start
                    if ans < tmp:
                        ans = tmp
                    start = end
print(ans)