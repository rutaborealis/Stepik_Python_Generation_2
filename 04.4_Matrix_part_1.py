# 4.4
# 4.4.1
n, m = int(input()), int(input())
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = input()

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

# 4.4.2
n, m = int(input()), int(input())
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = input()

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

print()

for j in range(m):
    for i in range(n):
        print(matrix[i][j], end=' ')
    print()

# 4.4.3
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
total = 0

for i in range(n):
    total += matrix[i][i]

print(total)

# 4.4.4
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
count = 0

for row in matrix:
    mean_row = sum(row) / len(row)
    for item in row:
        if item > mean_row:
            count += 1
    print(count)
    count = 0

# 4.4.5
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
maximum = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j) or (i >= j and i >= n - 1 - j):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

print(maximum)

# 4.4.6
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
maximum = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

print(maximum)

# 4.4.7
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0

for i in range(n):
    for j in range(n):
        if (i < j and i < n - 1 - j):
            sum_1 = sum_1 + matrix[i][j]
        if (i < j and i > n - 1 - j):
            sum_2 = sum_2 + matrix[i][j]
        if (i > j and i > n - 1 - j):
            sum_3 = sum_3 + matrix[i][j]
        if (i > j and i < n - 1 - j):
            sum_4 = sum_4 + matrix[i][j]

print(f'Верхняя четверть: {sum_1}\n'
      f'Правая четверть: {sum_2}\n'
      f'Нижняя четверть: {sum_3}\n'
      f'Левая четверть: {sum_4}')
