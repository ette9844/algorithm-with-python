# Q7 https://www.acmicpc.net/problem/18406
arr = list(map(int, input()))
len = len(arr)
half = len // 2

if sum(arr[:half]) == sum(arr[half:]):
  print('LUCKY')
else:
  print('READY')