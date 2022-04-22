# 문제 설명: p183
n, k = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1 = sorted(list1)
list2 = sorted(list2, reverse=True)
for i in range(k):
  # list1의 원소가 list2의 원소보다 작을 때만 교환
  if list1[i] < list2[i]:
    list1[i], list2[i] = list2[i], list1[i]
  # 원소가 크거나 같을 경우 반복문을 탈출
  else:
    break

# sum 함수로 원소의 합 출력
print(sum(list1))

"""
입력 예시
5 3
1 2 5 4 3 
5 5 6 6 5

출력 예시
26
"""