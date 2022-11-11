import sys
from collections import deque

def push_front(d, num):
    d.appendleft(num)
def push_back(d, num):
    d.append(num)
def pop_front(d):
    if len(d) == 0:
        print(-1)
    else:
        print(d.popleft())
def pop_back(d):
    if len(d) == 0:
        print(-1)
    else:
        print(d.pop())
def size(d):
    print(len(d))
def empty(d):
    if len(d) == 0:
        print(1)
    else:
        print(0)
def front(d):
    if d:
        print(d[0])
    else:
        print(-1)
def back(d):
    if d:
        print(d[-1])
    else:
        print(-1)

command_dic = {
    'push_front' : push_front,
    'push_back' : push_back,
    'pop_front' : pop_front,
    'pop_back' : pop_back,
    'size' : size,
    'empty' : empty,
    'front' : front,
    'back' : back
}

n = int(sys.stdin.readline())
d = deque()

for i in range(n):
    command = list(sys.stdin.readline().split())
    if len(command) == 2:
        cmd, num = command
        command_dic[cmd] (d, int(num))
    else:
        command_dic[command[0]] (d)
