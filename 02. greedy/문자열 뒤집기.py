# https://www.acmicpc.net/problem/1439
arr = list(map(int, input()))

result = 0
before = arr[0]
for i in arr:
  now = arr[i]
  if now != before & now != arr[0]:
    result += 1

print(result)