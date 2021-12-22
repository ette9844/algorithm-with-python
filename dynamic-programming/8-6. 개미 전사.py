# 문제 설명: p221
# 점화식: ai = max((ai-2 + k[i]), (ai-1))
n = int(input())
k = list(map(int, input().split()))

d = [0] * 100
d[0] = k[0]
# d[1] = k[1] 오류!
d[1] = max(k[0], k[1]) # 정답

for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + k[i])

print(d[n - 1])

"""
입력 예시
4
1 3 1 5

출력 예시
8
"""