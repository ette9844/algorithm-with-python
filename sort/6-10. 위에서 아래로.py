# 문제 설명: p179 위에서 아래로
n = int(input())
datalist = []
for i in range(n):
  datalist.append(int(input()))

datalist = sorted(datalist, reverse=True)
for i in datalist:
  print(i, end=' ')

# 수의 개수가 500개 이하로 적음, 모든 수는 1~100,000 로 기본 정렬 라이브러리를 사용하는 것이 효과적