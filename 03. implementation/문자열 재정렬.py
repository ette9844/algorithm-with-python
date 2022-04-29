# Q8 p323
import heapq
str = input()

q = []
sum = 0
for x in str:
  if x.isdigit():
    sum += int(x)
  else:
    heapq.heappush(q, x)

while q:
  print(heapq.heappop(q), end='')
if sum != 0:
  print(sum)

"""
입력
K1KA5CB7
출력
ABCKK13

입력
AJKDLSI412K4JSJ9D
출력
ADDIJJJKKLSS20
"""