x, y = map(int, input().split())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
w = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day_s = 0
for i in range(x-1):
    day_s += days[i]

day_s += y
print(w[day_s%7])
