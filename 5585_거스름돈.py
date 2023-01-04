n = int(input())
c = 1000-n
ans = 0
ans += c//500
c = c%500
ans += c//100
c = c%100
ans += c//50
c = c%50
ans += c//10
c = c%10
ans += c//5
c = c%5
ans += c//1
print(ans)