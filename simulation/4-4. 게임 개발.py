# 문제 정보: p119 게임 개발
n, m = map(int, input().split())
x, y, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

# 서 남 동 북
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d = 3 - d
nx, ny = 0, 0
count, turn = 1, 0
map[x][y] = 1

while True:
  d = int((d + 1) % 4)
  nx = x + dx[d]
  ny = y + dy[d]
  if nx < 0 or ny < 0 or nx >= n or ny >= m:
    continue
  if map[nx][ny] == 0:
    map[x][y] = 1
    x, y = nx, ny
    count += 1
    turn = 0
  else:
    turn += 1
    if turn == 4:
      break

print(count)

# 틀린 점: 가본 칸과 바다인 칸의 구분이 되어야 함 (뒤로가는 조건이 반영되지 않음)