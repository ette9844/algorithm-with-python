# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
  answer = len(s)
  for unit in range(1, len(s) // 2 + 1):
    compressed = ""
    prev = s[0:unit]
    count = 1
    for j in range(unit, len(s), unit):
      curr = s[j:j + unit]
      if curr != prev:
        compressed += str(count) + prev if count >= 2 else prev
        prev = curr
        count = 1
      else:
        count += 1
    # 남은 문자열 처리
    compressed += str(count) + prev if count >= 2 else prev
    answer = min(answer, len(compressed))
  return answer