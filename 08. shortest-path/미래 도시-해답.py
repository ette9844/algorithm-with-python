# 문제 설명: p260
# N의 범위가 100이하로 매우 한정적이기 때문에 구현이 빠른 플로이드 워셜 알고리즘을 사용하는 것이 유리
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for i in range(n + 1)]

for a in range(1, n + 1):
  graph[a][a] = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1 # 양방향
  graph[b][a] = 1

x, k = map(int, input().split())
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
  print(-1)
else:
  print(distance)

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