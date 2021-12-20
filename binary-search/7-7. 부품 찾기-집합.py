# 문제 설명: p198
n = int(input())
# 입력을 집합 자료형에 기록
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if i in array:
    print("yes", end=" ")
  else:
    print("no", end=" ")

"""
입력 예시
5
8 3 7 9 2
3
5 7 9

출력 예시
no yes yes
"""