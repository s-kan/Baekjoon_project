n = int(input())
num_card = list(map(int, input().split()))
num_card.sort()
m = int(input())
search_card = list(map(int, input().split()))

num_card_dict = {}
for i in num_card:
    if i in num_card_dict:
        num_card_dict[i] += 1
    else:
        num_card_dict[i] = 1

for i in search_card:
    if i in num_card_dict:
        print(num_card_dict[i], end=' ')
    else:
        print(0, end=' ')