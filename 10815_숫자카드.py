n = int(input())
n_arr = list(map(int, input().split()))
n_set = set(n_arr)
m = int(input())
m_arr = list(map(int, input().split()))


for i in m_arr:
    if i in n_set:
        print(1, end=' ')
    else:
        print(0, end=' ')
        