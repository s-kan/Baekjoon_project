n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)

print(arr[0]*arr[-1])

