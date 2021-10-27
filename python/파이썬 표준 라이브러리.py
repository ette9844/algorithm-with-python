# 자주 사용되는 파이썬 표준 라이브러리
# 1. 내장 함수: print(), input(), sorted(), sum(), min(), max(), eval()...
# 2. itertools: 반복되는 형태의 데이터를 처리하는 라이브러리 (순열, 조합...)
# 3. heapq: 힙 라이브러리, 우선순위 큐 구현에 사용됨
# 4. bisect: 이진 탐색 라이브러리
# 5. collections: 덱(deque), 카운터 자료구조 라이브러리
# 6. math: 수학 연산 라이브러리 (팩토리얼, 제곱근, GCD, 삼각함수, pi...)


# 내장 함수 ----------------------------------------------------------
print(sum([1, 2, 3, 4, 5]))
print(min([1, 2, 3, 4, 5]))
print(max(1, 2, 3, 4, 5))
print(eval("(3+5)*7"))

print(sorted([9, 1, 8, 5, 4]))
print(sorted([9, 1, 8, 5, 4], reverse = True))

print(sorted([('hong', 75), ('lee', 23), ('kim', 58)], key = lambda x: x[1], reverse = True))

data = [9, 1, 8, 5, 4]
data.sort()
print(data)


# itertools ---------------------------------------------------------
# permutations = 순열
# list 에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우
from itertools import permutations
data = [9, 4, 1]
result = list(permutations(data, 2))
print(result)

# combinations = 조합
# list 에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우
from itertools import combinations
result = list(combinations(data, 2))
print(result)

# product = 중복을 포함하는 순열
from itertools import product
result = list(product(data, repeat=2))
print(result)

# combinations_with_replacement = 중복을 허용하는 조합
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
print(result)


# heapq -------------------------------------------------------------
# 파이썬의 힙은 최소 힙으로 구성되어있음. 
# 힙에 넣었다 빼는 것 만으로 O(NlogN) 오름차순 정렬 완성
# 최소 힙의 최상단 원소는 항상 가장 작은 원소
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# heapq 로 최대 힙 구현
# 부호를 바꿔 정렬 후 복구
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# bisect ------------------------------------------------------------
# 이진 탐색을 쉽게 구현하는 라이브러리
# 정렬된 배열에서 특정 원소를 찾아야할 때 효과적
# O(logN)

# bisect_left(a, x): 정렬을 유지하면서 리스트에 a에 데이터 x를 삽입할 가장 왼쪽 인덱스
# bisect_right(a, x): 정렬을 유지하면서 리스트에 a에 데이터 x를 삽입할 가장 오른쪽 인덱스
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 6]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

# 정렬된 리스트에서 값이 특정 범위에 속하는 원소 개수 구하기 O(logN)
from bisect import bisect_left, bisect_right

def count_by_range(list, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 4, 4, 5, 6, 6]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))


# deque -------------------------------------------------------------
# Queue 구현 라이브러리
# 리스트와 달리 앞쪽에 있는 원소를 추가하고 삭제할때도 O(1)의 시간만 소요됨
# 인덱싱, 슬라이싱 불가, 나열된 데이터의 시작과 끝에 데이터를 삽입/삭제 할 때 효과적
# 스택과 큐 자료구조 대용으로 사용
# 큐 = deque.append(), .popleft() = FIFO
# 스택 = deque.append(), .pop() = LIFO
from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data))

# Counter: 리스트 데이터에서 원소가 몇번씩 등장했는지를 알려주는 자료형
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))