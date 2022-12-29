s = input()
ans = []
for i in s:
	if 65 <= ord(i) <= 90:
		if 90< ord(i)+13:
			ans.append(chr(ord(i)+13-90+64))
		else:
			ans.append(chr(ord(i)+13))
	elif 97 <= ord(i) <= 122:
		if 122 < ord(i)+13:
			ans.append(chr(ord(i)+13-122+96))
		else:
			ans.append(chr(ord(i)+13))
	else:
		ans.append(i)
result = ''.join(ans)
print(result)