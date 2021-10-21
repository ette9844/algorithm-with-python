n, m = map(int, input().split())

result = 0
while True:
    # // 연산자: 나누기 연산의 몫 (소수점 아래를 제거)
    target = (n // m) * m
    result += n - target
    n = target
    if n < m:
        break
    n //= m
    result += 1

result += n - 1
print(result)
