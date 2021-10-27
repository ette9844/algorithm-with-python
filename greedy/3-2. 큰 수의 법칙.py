n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

sum = 0
count = 0

i = m / (k + 1)
j = m % (k + 1)
z = numbers[0] * k + numbers[1]

sum = int(i * z + j * numbers[0])
print(sum)

