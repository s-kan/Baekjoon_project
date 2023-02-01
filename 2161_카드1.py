from collections import deque

n = int(input())
trash = []
cards = [i for i in range(1, n+1)]
cards = deque(cards)

idx = 0
while cards:
    if idx == 0:
        trash.append(cards.popleft())
        idx += 1
    else:
        cards.append(cards.popleft())
        idx -= 1
print(' '.join(map(str, trash)))