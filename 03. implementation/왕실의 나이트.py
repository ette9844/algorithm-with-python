# 문제 정보: p116 왕실의 나이트
pos = input()

x = int(pos[1])
y = int(ord(pos[0])- ord('a')) + 1

count = 0
dirs = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

for dir in dirs:
    nx = x + dir[1]
    ny = y + dir[0]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count += 1
    
print(count)