N = int(input())

A = []
for i in range(N):
    A.append(input()+" ")

for i in A:
    N = 0
    C = 0
    for j in i:
        if j == 'O':
            N = N+1
        else:
            for i in range(1,N+1):
                C = C+i
                N = 0
    print(C)

