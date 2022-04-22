# 문제 설명: p198
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아 기록
for i in input().split():
  array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if array[i] == 1:
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