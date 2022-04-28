# p315
# n 개의 동전으로 만들 수 없는 양의 정수 금액 중 최솟값
n = int(input())
data = list(map(int, input().split()))

data.sort()
result, last, sum = 0
for i in range(len(data)):
  now = data[i]
  if sum < now:
    break
  sum += now

result = sum + 1
print(result)