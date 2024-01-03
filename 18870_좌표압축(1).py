# Use enumerate

import sys

sys.stdin.readline()
arr = list(map(int, sys.stdin.readline().split()))

ans_dict = {x: i for i, x in enumerate(sorted(set(arr)))}
print(' '.join([str(ans_dict[num]) for num in arr]))