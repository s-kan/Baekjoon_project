import sys

N = int(sys.stdin.readline())
s = set(sys.stdin.readline().split())
M = int(sys.stdin.readline())
s_t = sys.stdin.readline().split()

for i in s_t:
    sys.stdout.write('1\n') if i in s else sys.stdout.write('0\n')