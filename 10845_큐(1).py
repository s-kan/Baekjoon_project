import sys
n = int(sys.stdin.readline())

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, num):
        self.queue.append(num)

    def pop(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[0])
            del self.queue[0]

    def size(self):
        print(len(self.queue))

    def isEmpty(self):
        if len(self.queue) == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[0])

    def back(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[-1])

q = Queue()
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        q.push(int(s[1]))
    elif s[0] == 'pop':
        q.pop()
    elif s[0] == 'size':
        q.size()
    elif s[0] == 'empty':
        q.isEmpty()
    elif s[0] == 'front':
        q.front()
    elif s[0] == 'back':
        q.back()