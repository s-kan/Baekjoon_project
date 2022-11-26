testcase = int(input())

result = []
for i in range(testcase):
    n, m = map(int, input().split())
    pri = list(map(int, input().split()))
    cnt = 0
    while(1):
        if pri[0] < max(pri):
            pri.append(pri.pop(0))
            if m == 0:
                m = len(pri)-1
            else:
                m -= 1
        else:
            pri.pop(0)
            if m == 0:
                result.append(cnt+1)
                break
            else:
                m -= 1
                cnt += 1

for i in result:
    print(i)