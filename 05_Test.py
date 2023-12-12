# 5 Test
import numpy as np

# 5.1
text = input().split()
n = int(input())
result = [[] for _ in range(n)]
remainder = 0

for _ in range(n):
    for i in range(len(text)):
        if i % n == remainder:
            result[remainder].append(text[i])
    remainder += 1

print(result)

# 5.2
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
maximum = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (i <= j and i >= n - 1 - j) or (i >= j and i >= n - 1 - j):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

print(maximum)

# 5.3
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

matrix_transpose = np.transpose(matrix)

for row in matrix_transpose:
    print(*row)

# 5.4
n = int(input())
matrix = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i == n // 2) or (j == n // 2) or (i == j) or (i == n - j - 1):
            matrix[i][j] = '*'

for row in matrix:
    print(*row)

# 5.5
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

matrix_transpose = [[matrix[i][j] for i in range(n - 1, -1, -1)] for j in range(n - 1, -1, -1)]

if matrix == matrix_transpose:
    print('YES')
else:
    print('NO')

# 5.6
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
numbers = list(range(1, n + 1))
result = 'YES'

for i in range(n):
    row_nums = sorted(matrix[i])
    col_nums = sorted([matrix[j][i] for j in range(n)])
    if row_nums != numbers or col_nums != numbers:
        result = 'NO'
        break

print(result)

# 5.7
matrix = [['.'] * 8 for _ in range(8)]
xy = input()
x = '87654321'.index(xy[1])
y = 'abcdefgh'.index(xy[0])
matrix[x][y] = 'Q'

for i in range(8):
    for j in range(8):
        if ((abs(x - i) > 0 and abs(y - j) == 0) or
                (abs(x - i) == 0 and abs(y - j) > 0) or
                (abs(x - i) == abs(y - j) != 0)):
            matrix[i][j] = '*'
        print(matrix[i][j], end=' ')
    print()

# 5.8
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = abs(i - j)
        print(matrix[i][j], end=' ')
    print()
