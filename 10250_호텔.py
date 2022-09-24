import sys
T = int(sys.stdin.readline())
HWN = []
for i in range(T):
    HWN.append(list(map(int, sys.stdin.readline().split())))

for i in range(T):
    w = int((HWN[i][2]-1)/HWN[i][0])+1
    h = HWN[i][2]%HWN[i][0]
    if h == 0:
        h = HWN[i][0]
    print(h*100+w)

