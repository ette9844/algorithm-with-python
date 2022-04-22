# 2. 개선된 다익스트라 알고리즘
"""
시간 복잡도: O(ElogV) V-노드 수 E-간선 수
힙 자료구조를 사용해 가장 거리가 짧은 노드를 빠르게 찾을 수 있다.

<힙>
우선순위 큐를 구현하기 위해 사용하는 자료구조
우선순위가 가장 높은 데이터를 먼저 삭제한다
데이터를 우선순위에 따라 처리하고 싶을 때 사용

우선순위 큐 파이썬 라이브러리: PriorityQueue, heapq(★)
우선순위 큐에 데이터 묶음을 넣을 시, 첫번째 원소를 기준으로 우선순위를 설정한다. (가치, 물건) 형태로 값을 넣는다.

<최소 힙 or 최대 힙>
언어마다 우선순위 큐 구현 시 최소 힙을 사용하는지 최대 힙을 사용하는지 유의해야한다.

다익스트라 알고리즘의 경우 최소 비용 노드를 우선 방문하기 때문에 최소 힙을 사용하는 파이썬 우선순위 큐 라이브러리를 그대로 사용하면 적합

최소 힙을 최대 힙처럼 사용하기 위해서는 우선순위 값에 음수 부호(-)를 붙여 넣었다가 나중에 우선순위 큐에서 꺼낸 후 다시 음수 부호(-)를 붙여 원상 복귀하는 테크닉을 사용한다.
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1) # 최단 거리 테이블

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  # 시작 노드의 최단 경로를 0으로 설정하여 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q: # 큐가 비어있지 않다면
    # 최단 거리 노드 정보 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적 있는 노드라면 무시
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
  if distance[i] == INF:
    print("INFINITY") # 도달 불가
  else:
    print(distance[i]) # 도달 가능

