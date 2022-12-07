str = input()
result = 0
for i in str:
    aci = ord(i)
    if aci <= 67:
        result += 3
    elif 68 <= aci <= 70:
        result += 4
    elif 71 <= aci <= 73:
        result += 5
    elif 74 <= aci <= 76:
        result += 6
    elif 77 <= aci <= 79:
        result += 7
    elif 80 <= aci <= 83:
        result += 8
    elif 84 <= aci <= 86:
        result += 9
    elif 87 <= aci <= 90:
        result += 10
print(result)
