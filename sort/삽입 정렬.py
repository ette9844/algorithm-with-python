"""
insertion sort
특정한 데이터를 적절한 위치에 삽입, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정함.

시간 복잡도: O(N^2)
데이터가 거의 정렬되어 있을 때 효율적 O(N)

"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  # i부터 1까지 1씩 감소하며 반복
  for j in range(i, 0, -1):
    # 한 칸씩 왼쪽으로 이동
    if array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j]
    # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
    else:
      break

print(array)
