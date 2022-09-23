N = int(input())

f = int(N/5)
t = 0

while (1):
    M = N-5*f
    if M%3 == 0:
        t = int(M/3)
        break
    else:
        f = f-1
    if f<0:
        break

print(f+t)