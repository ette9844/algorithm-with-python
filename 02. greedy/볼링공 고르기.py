# p316
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11
for x in data:
  array[x] += 1  # 무게에 따른 볼링공 개수 카운트

result = 0
for i in range(1, m + 1):
  n -= array[i]  # 조합 검사이기 때문에 이미 계산한 경우는 제외
  # (A가 선택할 수 있는 개수) * (B가 선택할 수 있는 개수)
  result += array[i] * n

print(result)

"""
입력
5 3
1 3 2 3 2
출력
8

입력
8 5
1 5 4 3 2 4 5 2
출력
25
"""