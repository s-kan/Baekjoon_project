import sys

n = int(sys.stdin.readline())
def add(x):
    s.add(x)
def remove(x):
    if x in s:
        s.remove(x)
def check(x):
    if x in s:
        print(1)
    else:
        print(0)
def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)
def all():
    return set([i for i in range(1, 21)])

def empty():
    return set()

cmd = {
    'add' : add,
    'remove' : remove,
    'check' : check,
    'toggle' : toggle,
    'all' : all,
    'empty' : empty
}
s = set()

for i in range(n):
    c = list(sys.stdin.readline().split())
    if len(c) == 2:
        cmd[c[0]](int(c[1]))
    else:
        s = cmd[c[0]]()
