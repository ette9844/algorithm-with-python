# https://programmers.co.kr/learn/courses/30/lessons/42891
import heapq
def solution(food_times, k):
  # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
  if sum(food_times) <= k:
    return -1
  
  # 시간이 적게 소요되는 음식부터 처리 (우선순위 큐)
  length = len(food_times)  # 남은 음식 수
  q = []
  for i in range(length):
    heapq.heappush(q, (food_times[i], i + 1))

  sum_value = 0   # 먹기 위해 사용한 시간
  last = 0        # 직전에 다 먹은 음식 시간
  
  # 현재 음식을 다 먹는데 소요되는 시간과 k 비교
  while sum_value + ((q[0][0] - last) * length) <= k:
    now = heapq.heappop(q)[0]
    sum_value += (now - last) * length
    length -= 1
    last = now
  
  result = sorted(q, key = lambda x: x[1])
  return result[(k - sum_value) % length][1]

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))