# 문제 설명: p301
# http://www.acmicpc.net/problem/1647
n, m = map(int, input().split())
graph = []

def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

parent = [0] * (n + 1)
for i in range(1, n + 1):
  parent[i] = i

for _ in range(m):
  a, b, c = map(int, input().split())
  graph.append((c, a, b))

graph.sort()
result = 0
last = 0 # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선
for edge in graph:
  c, a, b = edge
  if find(parent, a) != find(parent, b):
    union(parent, a, b)
    result += c
    last = c

print(result - last) # 을 제외하여 두개의 신장 트리로 나눈다

"""
입력
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

출력
8
"""