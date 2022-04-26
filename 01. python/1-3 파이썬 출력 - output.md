# 파이썬 출력
```python
a = 1
b = 2

# 공백으로 구분되어 출력됨
print(a, b)

# 줄바꿈으로 구분되어 출력됨
print(a)
print(b)
```

## 문자열과 수를 함께 출력하기
```python
answer = 8
print("The answer is ... " + str(answer))
print("The answer is ...", answer)
print(f"The answer is ... {answer}") # python 3.6 이상 (f-string)
```