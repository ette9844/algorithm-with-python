# 문제설명: n시 59분 59초 까지 3이 포함된 횟수 출력
# 24시간은 86400초로 최대 연산수가 백만건을 넘지 않기 때문에 완전 탐색이 가능한 문제
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                count += 1
                
print(count)
