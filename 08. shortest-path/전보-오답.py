# 문제 설명: p263
INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  graph[i][i] = 0
for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x][y] = z

for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

count = 0
result = 0
for i in range(1, n + 1):
  if graph[c][i] < INF and c != i:
    count += 1
    result = max(result, graph[c][i])

print(count, result)

"""
입력 예시
3 2 1
1 2 4
1 3 2

출력 예시
2 4
"""