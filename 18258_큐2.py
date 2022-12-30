from collections import deque
import sys

n = int(sys.stdin.readline())
d = deque()
def push(a):
    d.append(a)
def pop():
    if len(d) == 0:
        return -1
    else:
        return d.popleft()
def size():
    return len(d)
def empty():
    if len(d) == 0:
        return 1
    else:
        return 0
def front():
    if len(d) == 0:
        return -1
    else:
        return d[0]
def back():
    if len(d) == 0:
        return -1
    else:
        return d[-1]

d = deque()
cmd = {
    'push' : push,
    'pop' : pop,
    'size' : size,
    'empty' : empty,
    'front' : front,
    'back' : back
}
for i in range(n):
    c = list(sys.stdin.readline().rstrip().split())
    if len(c) == 2:
        cmd[c[0]](int(c[1]))
    else:
        print(cmd[c[0]]())