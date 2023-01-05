arr = [sum(map(int, input().split())) for _ in range(3)]
d = {3:'A', 2:'B', 1:'C', 0:'D', 4:'E'}
for i in range(3):
    print(d[arr[i]])