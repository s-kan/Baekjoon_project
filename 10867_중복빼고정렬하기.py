n = int(input())
arr = list(map(int, input().split()))
arr = set(arr)
arr = sorted(arr)
print(' '.join(map(str, arr)))