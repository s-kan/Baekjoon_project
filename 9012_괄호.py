N = int(input())
A = []

for i in range(N):
    A.append((list(input())))

for j in A:
    l = 0
    r = 0
    if j[0] == ')' or j[-1] == '(' or j.count('(') != j.count(')'):
        print('NO')
    else:
        for k in j:
            if k == '(':
                l = l+1
            else:
                r = r+1
                if r > l:
                    print('NO')
                    break
                elif r+l == len(j):
                    print("YES")