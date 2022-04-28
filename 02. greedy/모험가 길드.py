# 문제 설명: p312
n = int(input())
data = list(map(int, input().split()))
result = 0
count = 0

data.sort()
for i in data:
  count += 1
  if i <= count:
    result += 1
    count =0

print(result)
"""
입력
5
2 3 1 2 2

출력
2
"""