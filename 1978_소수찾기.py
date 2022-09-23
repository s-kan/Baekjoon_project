N = int(input())
arr = list(map(int, input().split()))
c=0

for i in arr:
    if i==1:
        continue
    elif i==2:
        c=c+1
    else:
        for j in range(2, i):
            if i%j == 0:
                break
            elif i-1 == j:
                c = c+1
print(c)