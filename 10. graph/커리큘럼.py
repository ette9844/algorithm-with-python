# cost 가 큰 순으로 위상 정렬
from collections import deque
import copy
n = int(input())
indegree = [0] * (n + 1)
time = [0] * (n + 1)
graph = [[] for i in range(n + 1)]

for i in range(1, n + 1):
  arr = list(map(int, input().split()))
  time[i] = arr[0]
  for j in arr[1:-1]:
    graph[j].append(i)
    indegree[i] += 1

q = deque()
for i in range(1, n + 1):
  if indegree[i] == 0:
    q.append(i)

result = copy.deepcopy(time)
while q:
  now = q.popleft()
  for a in graph[now]:
    result[a] = max(result[a], result[now] + time[a])
    indegree[a] -= 1
    if indegree[a] == 0:
      q.append(a)

for i in range(1, n + 1):
  print(result[i])

"""
입력
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

출력
10
20
14
18
17
"""