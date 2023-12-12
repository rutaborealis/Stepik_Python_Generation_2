# 4.7
import numpy as np

# 4.7.1
n, m = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(n)]
input()
B = [[int(i) for i in input().split()] for _ in range(n)]

result = np.add(A, B)

for row in result:
    print(*row)

# 4.7.2
n, m = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, K = map(int, input().split())
B = [[int(i) for i in input().split()] for _ in range(m)]

result = np.dot(A, B)

for row in result:
    print(*row)

# 4.7.3
n = int(input())
A = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())

result = np.linalg.matrix_power(A, m)

for row in result:
    print(*row)