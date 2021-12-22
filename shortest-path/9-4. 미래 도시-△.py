# 문제 설명: p260
# 다익스트라 알고리즘
import heapq
n, m = map(int, input().split())
INF = int(1e9)
graph = [[] for i in range(n + 1)]

for _ in range (m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

x, k = map(int, input().split())

def dijkstra(start, end):
  distance = [INF] * (n + 1) # 최단 거리 테이블
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + 1
      if cost < distance[i]:
        distance[i] = cost
        heapq.heappush(q, (cost, i))
  return distance[end]

result = dijkstra(1, k) + dijkstra(k, x)
if result >= INF:
  print(-1)
else:
  print(result)

"""
입력 예시1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

출력 예시1
3

입력 예시2
4 2
1 3
2 4
3 4

출력 예시2
-1
"""