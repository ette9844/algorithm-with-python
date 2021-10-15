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