# 문제 설명: p299
n, m = map(int, input().split())

def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def merge(parent, a, b):
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
  oper, a, b = map(int, input().split())
  if oper == 0:
    merge(parent, a, b)
  elif oper == 1:
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
      print("NO")
    else:
      print("YES")

"""
입력
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

출력
NO
NO
YES
"""