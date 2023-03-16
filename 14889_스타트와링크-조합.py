import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
member_all = list(range(n))
answer = int(1e9)

for start_member in list(combinations(member_all, n//2)):
    start_total = link_total = 0
    link_member = list(set(member_all) - set(start_member))
    for i, j in list(combinations(start_member, 2)):
        start_total += arr[i][j]
        start_total += arr[j][i]
    for i, j in list(combinations(link_member, 2)):
        link_total += arr[i][j]
        link_total += arr[j][i]
    answer = min(answer, abs(start_total-link_total))

print(answer)