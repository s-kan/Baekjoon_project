n = int(input())
for i in range(n):
	s = input().split()
	for i in s:
		tmp = ''.join(reversed(i))
		print(tmp, end=' ')
	print()