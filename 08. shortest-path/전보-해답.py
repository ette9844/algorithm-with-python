# 문제 설명: p263
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra(start):
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(c)
count = 0
result = 0
for i in distance:
  if i > 0 and i < INF:
    count += 1
    result = max(result, i)
print(count, result)

"""
입력 예시
3 2 1
1 2 4
1 3 2

출력 예시
2 4
"""