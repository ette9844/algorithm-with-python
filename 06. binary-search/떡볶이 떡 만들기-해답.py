# 문제 설명: p202
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
  total = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      total += x - mid
  # 떡 양이 부족한 경우 더 많이 자르기 (왼쪽 탐색)
  if total < m:
    end = mid - 1
  # 떡 양이 충분한 경우 덜 자르기 (오른쪽 탐색)
  else:
    # 최대한 덜 자른쪽이 정답이기 때문에 이 시점에서 result에 기록
    result = mid
    start = mid + 1

print(result)

"""
입력 예시
4 6
19 15 10 17

출력 예시
15
"""