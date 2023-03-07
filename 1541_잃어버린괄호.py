s = input()
arr = []
left = 0
for i in range(len(s)):
    if s[i] == '-' or s[i] == '+':
        arr.append(int(s[left:i]))
        arr.append(s[i])
        left = i+1
    if i == len(s)-1:
        arr.append(int(s[left:]))

idx = 0
ans = 0
while idx < len(arr):
    if arr[idx] == '-':
        while True:
            idx += 1
            if arr[idx] != '+' and arr[idx] != '-':
                ans -= arr[idx]
            if idx == len(arr)-1:
                idx += 1
                break
            if arr[idx] == '-':
                break
    else:
        if arr[idx] != '+':
            ans += arr[idx]
        idx += 1
print(ans)