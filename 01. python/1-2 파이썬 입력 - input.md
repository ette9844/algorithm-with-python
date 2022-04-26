# 파이썬 입력
## 일반 입력
```python
one_input = int(input())
list_input = list(map(int, input().split()))
one, two, three = map(int, input().split())
```

## 대량의 입력을 받아야할 때
```python
import sys
massive_data = sys.stdin.readline().rstrip()
print(massive_data)
```

## List comprehension 으로 2차원 배열 입력받기
https://minjoos.tistory.com/2
```python
map = [list(map(int, input().split())) for _ in range(3)]
```