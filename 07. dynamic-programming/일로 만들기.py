# 문제 설명: p218
# 점화식: ai = min(ai-1, ai/2, ai/3, ai/5) + 1
x = int(input())
d = [0] * 30001 # DP 테이블 초기화

for i in range(2, x + 1):
  d[i] = d[i - 1] + 1
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

"""
입력 예시
26

출력 예시
3
"""