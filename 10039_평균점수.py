scores = [int(input()) for i in range(5)]

for i in range(5):
    if scores[i] < 40:
       scores[i] = 40

print(sum(scores)//5)