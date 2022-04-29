# BFS 
**너비 우선 탐색**  
가까운 노드부터 탐색하는 알고리즘  
큐를 이용해 구현  

시간 복잡도: **O(N)**

python에서는 deque 라이브러리를 사용하여 구현하는 것이 좋다.
재귀함수로 구현한 DFS보다 수행 시간이 빠르다.

## 원리
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복

```python
from collections import deque

# 기본 BFS 탐색 함수
def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  # queue 가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑기
    v = queue.popleft()
    print(v, end=' ')
    # 해당 원소와 연결된 미방문 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 예제 그래프
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# BFS 함수 호출
visited = [False] * 9
bfs(graph, 1, visited)
```