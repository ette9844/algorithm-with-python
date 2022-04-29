# 문제 설명: p154 미로 탈출
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# bfs는 연결된 노드부터 탐색하므로 최소 루트 문제에 적합
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


bfs(0, 0)
print(graph[n - 1][m - 1])