# 6.3
import math

# 6.3.1
numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
result = math.prod(numbers)
print(result)

# 6.3.2
data = 'Python для продвинутых!'
print(tuple(data))

# 6.3.3
poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
poet_data = list(poet_data)
poet_data[2] = 'Москва'
poet_data = tuple(poet_data)
print(poet_data)

# 6.3.4
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
result = []

for row in numbers:
    result.append(sum(row) / len(row))

print(result)

# 6.3.5
a, b, c = int(input()), int(input()), int(input())

x0 = -b / (2 * a)
y0 = (4 * a * c - b ** 2) / (4 * a)
top_of_parabola = tuple([x0, y0])

print(top_of_parabola)

# 6.3.6
students = [input().split() for _ in range(int(input()))]

for i in range(len(students)):
    students[i][1] = int(students[i][1])
    students[i] = tuple(students[i])
    print(*students[i])

print()

for row in students:
    if row[1] == 4 or row[1] == 5:
        print(*row)

# 6.3.7
n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end = ' ')
    f1, f2, f3 = f2, f3, f1 + f2 + f3
