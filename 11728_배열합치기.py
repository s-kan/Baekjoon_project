import sys

n, m = map(int, sys.stdin.readline().split())
print(' '.join(sorted(sys.stdin.readline().split()+sys.stdin.readline().split(), key=int)))

