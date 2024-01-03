import sys

scores = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5,
          'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
mul_scores = 0
sum_cred = 0
for _ in range(20):
    a, b, c = sys.stdin.readline().split()
    if c == 'P':
        # sum_cred += float(b)
        continue
    mul_scores += float(b) * scores[c]
    sum_cred += float(b)
print(mul_scores/sum_cred)