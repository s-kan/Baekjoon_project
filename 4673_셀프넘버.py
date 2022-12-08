self_dic = {i:1 for i in range(10001)}

for i in range(10001):
    if i<10:
        a = i
        r = i+a
        self_dic[r] = 0
    elif 10 <= i <100:
        a = i//10
        b = i%10
        r = i + a + b
        self_dic[r] = 0
    elif 100 <= i < 1000:
        a = i//100
        b = i%100//10
        c = i%10
        r = i + a + b + c
        self_dic[r] = 0
    elif 1000 <= i < 10000:
        a = i//1000
        b = i%1000//100
        c = i%100//10
        d = i%10
        r = i + a + b + c + d
        if r>10000:
            continue
        else:
            self_dic[r] = 0

for i in range(10001):
    if self_dic[i] == 1:
        print(i)