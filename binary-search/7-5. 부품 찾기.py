# 문제 설명: p198
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

def binary_search(array, target):
  start = 0
  end = len(array)
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return True
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return False

for i in b:
  if binary_search(a, i):
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