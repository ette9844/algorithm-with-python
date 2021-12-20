# 문제 설명: p202

# 오답: 시간초과 - n이 최대 100만 개이므로 순차 탐색으로 연산할 경우 시간초과가 발생한다.
n, m = map(int, (input().split()))
a = list(map(int, input().split()))

a.sort(reverse=True)
cut = a[0]
while True:
  sum = 0
  cut -= 1
  for i in range(0, n):
    if cut >= a[i]:
      break
    sum += a[i] - cut
  if sum >= m:
    break

print(cut)


"""
입력 예시
4 6
19 15 10 17

출력 예시
15
"""