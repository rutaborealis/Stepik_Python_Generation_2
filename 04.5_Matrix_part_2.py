# 4.5
# 4.5.1
n, m = int(input()), int(input())
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * j
        print(str(matrix[i][j]).ljust(3), end='')
    print()

# 4.5.2
n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
maximum = matrix[0][0]
index_i = 0
index_j = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            index_i = i
            index_j = j

print(index_i, index_j)

# 4.5.3
n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
col1, col2 = map(int, input().split())

for i in range(n):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

for row in matrix:
    print(*row)

# 4.5.4
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')

# 4.5.5
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]

for row in matrix:
    print(*row)

# 4.5.6
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

matrix.reverse()

for row in matrix:
    print(*row)

# 4.5.7
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

matrix.reverse()

for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()

# 4.5.8
n = 8
matrix = [['.'] * n for _ in range(n)]

xy = input()
x = '87654321'.index(xy[1])
y = 'abcdefgh'.index(xy[0])
matrix[x][y] = 'N'

for i in range(n):
    for j in range(n):
        index = (x - j) * (y - i)
        if index == 2 or index == -2:
            matrix[j][i] = '*'

for row in matrix:
    print(*row)

# 4.5.9
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

checking_sum = sum(matrix[0])
checking_flag = True
checking_list = [num for num in range(1, n ** 2 + 1)]

matrix_list = []
for i in range(n):
    for j in range(n):
        matrix_list.append(matrix[i][j])

for num in checking_list:
    if num not in matrix_list:
        checking_flag = False
        break

if checking_flag:
    for row in matrix:
        if sum(row) != checking_sum:
            checking_flag = False
            break

if checking_flag:
    for i in range(n):
        sum = 0
        for j in range(n):
            sum = sum + matrix[j][i]
        if sum != checking_sum:
            checking_flag = False
            break

if checking_flag:
    sum = 0
    for i in range(n):
        sum = sum + matrix[i][i]
    if sum != checking_sum:
        checking_flag = False

if checking_flag:
    sum = 0
    for i in range(n):
        sum = sum + matrix[n - 1 - i][i]
    if sum != checking_sum:
        checking_flag = False

if checking_flag:
    print('YES')
else:
    print('NO')