"""
selection sort
데이터 중 가장 작은 데이터를 선택해 맨앞 데이터와 바꾸는 것을 반복
시간 복잡도: O(N^2)

"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  # 가장 작은 원소 찾기
  min_index = i
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  # 스와프
  array[i], array[min_index] = array[min_index], array[i]

print(array)
