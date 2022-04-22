"""
Disjoint Set 서로소 집합 자료구조

서로소 집합은 자료구조로서 그래프 알고리즘 전반에 사용된다.
서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조. (union-find 자료구조)

서로소 집합 연산
  1. union 합집합
  2. find 찾기

서로소 집합 연산은 그래프 형태로 표현 가능하다.
union 연산 알고리즘
  1. A와 B의 루트 노드 A', B'를 찾는다
  2. A'를 B'의 부모 노드로  설정한다.

find0은 find 연산이 최악의 경우 O(VM)이 되어 비효율적 6->5->4->3...
경로 압축 기법으로 최적화 할 수 있다.

경로 압축(Path Compression) 기법:
find 함수를 재귀적으로 호출한 뒤 부모 테이블 값을 갱신한다.
루트 노드가 부모 노드가 된다.
"""
# find 연산
def find0(parent, x):
  # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀 연산
  if parent[x] != x: 
    return find(parent, parent[x])
  return x
# 경로 압축 find 연산
def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

# union 연산
def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 입력 받기
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v + 1)
for i in range(v + 1):
  parent[i] = i

# union 연산 수행
for i in range(e):
  a, b = map(int, input().split())
  union(parent, a, b)

# 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
  print(find(parent, i), end=' ')
print()
print('부모 테이블: ', end='')
for i in range(1, v + 1):
  print(parent[i], end=' ')


"""
입력
6 4
1 4
2 3
2 4
5 6

출력
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 1 1 2 1 5 5
"""