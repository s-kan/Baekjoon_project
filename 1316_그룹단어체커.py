n = int(input())
words = [input() for i in range(n)]

cnt = 0
for i in words:
    state = 1
    vswords = set()
    vswords.add(i[0])
    if len(i) > 2:
        for j in range(1, len(i)):
            if i[j-1] != i[j]:
                if i[j] in vswords:
                    state = 0
                    break
            if j+1 == len(i):
                if i[j-1] != i[j] and i[j] in vswords:
                    state = 0
            vswords.add(i[j])
    if state == 1:
        cnt += 1

print(cnt)