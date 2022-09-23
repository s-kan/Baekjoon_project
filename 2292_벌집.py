N = int(input())
C = 1
n = 2
while(1):
    if N == 1:
        break
    elif n <= N < n+6*C:
        C = C+1
        break
    else:
        n = n+6*C
        C = C+1
print(C)