while True:
    str = input()
    if str == '0':
        break
    state = 0
    for i in range(len(str)//2):
        if str[i] != str[len(str)-1-i]:
            state = 1
            break
    if state == 0:
        print('yes')
    else:
        print('no')
