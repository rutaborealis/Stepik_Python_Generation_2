# 16 Test
from functools import reduce
from operator import *

# 16.1
def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    return f'''To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!'''

print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2', 'Василь Ярошевич', 23))

# 16.2
def pretty_print(data, side='-', delimiter='|'):
    s = f' {delimiter} '.join(map(str, data))
    print(' ', end='')

    for _ in range(len(s)+2):
        print(side, end='')

    print()
    print(delimiter, end=' ')
    print(s, end=' ')
    print(delimiter)
    print(' ', end='')

    for _ in range(len(s)+2):
        print(side, end='')
    print()

# 16.3
def concat(*args, sep=' '):
    result = str(args[0])
    for k, v in enumerate(args):
        if k == 0:
            continue
        result += sep + str(v)
    return result

print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))

# 16.4
def product_of_odds(data):
    result_filter = list(filter(lambda i: i % 2 == 1, data))
    return reduce(lambda x, y: x * y, result_filter, 1)

# 16.5
words = 'the world is mine take a look what you have started'.split()
print(*map(lambda x: '"' + x + '"', words))

# 16.6
numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
print(*filter(lambda x: str(x) != str(x)[::-1], numbers))

# 16.7
numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12),
           (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)

print(sorted_numbers)

# 16.8
def call(func, *args):
    return func(*args)

def mul7(x):
    return x * 7

def add2(x, y):
    return x + y

def add3(x, y, z):
    return x + y + z

print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))

# 16.9
def compose(f, g):
    def res_compose(x):
        return f(g(x))
    return res_compose

def add3(x):
    return x + 3

def mul7(x):
    return x * 7

print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))

# 16.10
def arithmetic_operation(op):
    if op == '+':
        return add
    elif op == '-':
        return sub
    elif op == '*':
        return mul
    elif op == '/':
        return truediv

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))

# 16.11
print(*sorted(input().split(), key=lambda x: x.lower()))

# 16.12
def gamatria(word):
    word_upper = word.upper()
    result_ord = map(lambda x: ord(x) - ord('A'), word_upper)
    result = reduce(lambda x, y: x + y, result_ord, 0)
    return result

n = int(input())
arr = [input().strip() for word in range(n)]
arr.sort()
print(*sorted(arr, key=gamatria), sep='\n')

# 16.13
def ip_to_number(ip):
    arr = [int(i) for i in ip.split('.')]
    return arr[0] * 256 ** 3 + arr[1] * 256 ** 2 + arr[2] * 256 + arr[3]

n = int(input())
arr_ip = [input().strip() for _ in range(n)]
print(*sorted(arr_ip, key=ip_to_number), sep='\n')
