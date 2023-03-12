import sys
import math
input = sys.stdin.readline

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    row = n//2
    high = n-row
    while True:
        if isPrime(row) and isPrime(high):
            print(row, high)
            break
        else:
            row -= 1
            high += 1
