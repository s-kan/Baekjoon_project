while(1):
    a, b, c = sorted(map(int, input(). split()))
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if c**2 == a**2 + b**2:
            print("right")
        else:
            print("wrong")
