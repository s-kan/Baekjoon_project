n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort(reverse=True)
trees.append(0)

h = 0
sum = 0
for i in range(len(trees)):
    if sum+(i+1)*(trees[i]-trees[i+1])>=m:
        idx = i
        h = trees[i]
        break
    else:
        sum += (i+1)*(trees[i] - trees[i+1])

x = m-sum
y = x//(idx+1)
h -= y

if x%(idx+1)!=0:
    h-=1

print(h)