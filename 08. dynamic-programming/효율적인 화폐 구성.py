# 문제 설명: p224
"""
점화식:
1. ai-k 를 만드는 방법이 존재하는 경우, ai = min(ai, ai-k + 1)
2. ai-k 를 만드는 방법이 존재하지 않는 경우, ai = 10,001
"""
n, m = map(int, input().split())
array = []
for i in range(n):
  array.append(int(input()))

d = [10001] * (m + 1) # DP 테이블 초기화
d[0] = 0

for i in range(n):
  for j in range(array[i], m + 1):
    d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])

"""
입력 예시1
2 15
2
3

출력 예시1
5

입력 예시2
3 4
3
5
7

출력 예시2
-1
"""