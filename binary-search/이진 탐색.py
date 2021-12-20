"""
binary search
데이터가 이미 정렬되어있어야 사용할 수 있는 알고리즘
찾으려는 데이터와 중간점 위치의 데이터를 반복적으로 비교해서 데이터를 찾는다

시간 복잡도: O(logN)

이진 탐색 문제는 탐색 범위가 큰 상황에서의 탐색을 가정하는 문제가 많다. 탐색 범위가 2000만을 넘을 시 이진 탐색으로 접근

이진 탐색 문제는 입력 데이터가 많거나 탐색 범위가 넓기 때문에 
sys 라이브러리를 사용해 빠르게 입력 데이터를 처리해야한다.
sys.stdin.readline().rstrip()

"""

# 재귀 함수 구현
def binary_search1(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  # 찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search1(array, target, start, mid - 1)
  else:
    return binary_search1(array, target, mid + 1, end)

# 반복문 구현
def binary_search2(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_search1(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)