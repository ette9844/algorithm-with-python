# 문제 설명: p150 음료수 얼려 먹기
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
count = 0

# 이차원 배열을 그래프로 생각하기
def dfs(x, y):
  if x < 0 or y < 0 or x >=n or y >=m:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      count += 1

print(count)