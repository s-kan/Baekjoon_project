while True:
    str = input()
    if str == '.':
        break
    stack = []
    state = 0
    for i in str:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                state = 1
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                state = 1
                break
        elif i == ']':
            if len(stack) == 0:
                state = 1
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                state = 1
                break
    if len(stack) != 0 or state == 1:
        print('no')
    else:
        print('yes')
