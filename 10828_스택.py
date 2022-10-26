import sys
n = int(sys.stdin.readline())

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            x = self.stack[-1]
            self.stack.pop()
            return x

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack[-1]

s = Stack()

for i in range(n):
    arr = sys.stdin.readline().split()
    if arr[0] == 'push':
        s.push(int(arr[1]))
    elif arr[0] == 'pop':
        print(s.pop())
    elif arr[0] == 'size':
        print(s.size())
    elif arr[0] == 'empty':
        print(s.isEmpty())
    elif arr[0] == 'top':
        print(s.top())