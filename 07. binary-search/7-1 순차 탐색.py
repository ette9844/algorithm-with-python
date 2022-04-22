"""
sequential search
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법

시간 복잡도: 최악의 경우 O(N)

"""
def sequential_search(n, target, array):
  for i in range(n):
    if array[i] == target:
      return i + 1

input_data = input().split()
n = int(input_data[0])
target = input_data[1]
array = input().split()

print(sequential_search(n, target, array))