n = input()

for i in range(len(n)//10):
    print(n[i*10:i*10+10])
print(n[len(n)//10*10:])