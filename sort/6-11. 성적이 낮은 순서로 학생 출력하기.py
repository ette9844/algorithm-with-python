# 문제 설명: p181
# 계수 정렬
n = int(input())
datalist = []
for i in range(n):
  student = input().split()
  datalist.append((student[0], int(student[1])))

count = [''] * (101)

for i in range(len(datalist)):
  name = datalist[i][0]
  grade = datalist[i][1]
  count[grade]= count[grade] + name + ' '
for i in range(len(count)):
  if count[i] != '':
    print(count[i],end='')

# 기본 라이브러리 정렬
n = int(input())
datalist = []
for i in range(n):
  student = input().split()
  # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 튜플로 저장
  datalist.append((student[0], int(student[1])))

datalist = sorted(datalist, key=lambda student: student[1])

for student in datalist:
  print(student[0], end= ' ')