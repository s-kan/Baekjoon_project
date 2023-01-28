while True:
    n = int(input())
    if n == -1:
        break
    else:
        arr = []
        s = 0
        for i in range(1, n):
            if n%i == 0:
                arr.append(i)
                s += i
        if s == n:
            print(n, '=', ' + '.join(map(str, arr)))
        else:
            print(n, 'is NOT perfect.')