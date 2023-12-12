# 15.4
import math

# 15.4.1
def mean(sequence):
    mean = sum(sequence) / len(sequence)
    return mean

numbers = [(10, 10, 10),
           (30, 45, 56),
           (81, 39),
           (1, 2, 3),
           (12,),
           (1, 2, 99),
           (89, 9, 34),
           (10, 20, 30, -2),
           (50, 40, 50),
           (34, 78, 65),
           (-5, 90, -1, -5),
           (1, 2, 3, 4, 5, 6),
           (-9, 8, 4),
           (90, 1, -45, -21)]

print(min(numbers, key=mean))
print(max(numbers, key=mean))

# 15.4.2
def distance(point):
    distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
    return distance

points = [(-1, 1),
          (5, 6),
          (12, 0),
          (4, 3),
          (0, 1),
          (-3, 2),
          (0, 0),
          (-1, 3),
          (2, 0),
          (3, 0),
          (-9, 1),
          (3, 6),
          (8, 8)]

print(sorted(points, key=distance))

# 15.4.3
def sum_min_max(sequence):
    result = min(sequence) + max(sequence)
    return result

numbers = [(10, 10, 10),
           (30, 45, 56),
           (81, 80, 39),
           (1, 2, 3),
           (12, 45, 67),
           (-2, -4, 100),
           (1, 2, 99),
           (89, 90, 34),
           (10, 20, 30),
           (50, 40, 50),
           (34, 78, 65),
           (-5, 90, -1)]

print(sorted(numbers, key=sum_min_max))

# 15.4.4
athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

def sorted_by_param(n):
    def compare(item):
        return item[n - 1]

    return sorted(athletes, key=compare)

n = int(input())

for t in sorted_by_param(n):
    print(*t)

# 15.4.5
def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def own_sqrt(n):
    return n ** 0.5

def modul(n):
    return abs(n)

def sinus(n):
    return math.sin(n)

commands = {'квадрат': square, 'куб': cube, 'корень': own_sqrt, 'модуль': modul, 'синус': sinus}

n, command = int(input()), input()

print(commands[command](n))

# 15.4.6
def compare(item):
    result = [int(i) for i in list(item)]
    return sum(result)

numbers = input().split()

print(*sorted(numbers, key = compare))

# 15.4.7
def compare(item):
    result = [int(i) for i in list(str(item))]
    return sum(result)

numbers = [int(i) for i in input().split()]
numbers.sort()

print(*sorted(numbers, key = compare))
