word = input()

result = 0
i = 0
while(i<len(word)):
    if word[i:i+2] == 'c=':
        result += 1
        i += 2
    elif word[i:i+2] == 'c-':
        result += 1
        i += 2
    elif word[i:i+3] == 'dz=':
        result += 1
        i += 3
    elif word[i:i+2] == 'd-':
        result += 1
        i += 2
    elif word[i:i+2] == 'lj':
        result += 1
        i += 2
    elif word[i:i+2] == 'nj':
        result += 1
        i += 2
    elif word[i:i+2] == 's=':
        result += 1
        i += 2
    elif word[i:i+2] == 'z=':
        result += 1
        i += 2
    else:
        i += 1
        result += 1
print(result)