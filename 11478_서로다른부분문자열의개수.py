s = input()
tmp_set = set()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        tmp = s[i:j]
        tmp_set.add(tmp)
print(len(tmp_set))