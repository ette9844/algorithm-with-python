# 문제 설명: p313
data = list(map(int, input()))

# 연산을 수행하는 두 인자 중 하나라도 0, 1 인 경우에는 덧셈이 유리
result = data[0]
for i in range(1, len(data)):
  num = data[i]
  if result <=1 or num <= 1:
    result += num
  else:
    result *= num

print(result)

"""
입력
02984
출력
576

입력
567
출력
210
"""